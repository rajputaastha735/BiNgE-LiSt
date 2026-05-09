import os
import base64
import io
from fastapi import FastAPI, HTTPException, Form, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, PermissionDenied, GoogleAPIError

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_key_here":
    raise RuntimeError("GEMINI_API_KEY environment variable is missing or not set correctly in .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize FastAPI app
app = FastAPI(title="BiNgE LiSt")

# System instruction for the chatbot
SYSTEM_INSTRUCTION = """
You are BiNgE LiSt, a knowledgeable, enthusiastic, and helpful movie and anime specialist.
Your goal is to answer questions about movies and anime (recommendations, plot analysis, content ratings, watch orders, streaming info, production trivia).
Be genuinely helpful and do not act like a paranoid corporate assistant.
You MUST:
- Answer general domain questions with enthusiasm.
- Add appropriate disclaimers where relevant (e.g., "streaming availability changes by region").
- Refuse ONLY: requests for serious harm, off-topic requests (e.g., coding, medical diagnoses), requests for piracy links, and explicit adult content.
If asked about something off-topic, politely redirect the conversation back to movies or anime.
"""

# Define Pydantic models for request bodies
class ChatPart(BaseModel):
    text: str

class ChatMessage(BaseModel):
    role: str
    parts: List[ChatPart]

class ChatRequest(BaseModel):
    message: str
    history: List[ChatMessage]

@app.get("/")
async def serve_frontend():
    return FileResponse("code.html")

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-lite",
            system_instruction=SYSTEM_INSTRUCTION
        )
        
        # Convert history format
        formatted_history = []
        for msg in req.history:
            parts = [{"text": p.text} for p in msg.parts]
            # Map frontend roles to Gemini roles if needed (usually 'user' and 'model')
            role = "user" if msg.role == "user" else "model"
            formatted_history.append({"role": role, "parts": parts})
            
        chat = model.start_chat(history=formatted_history)
        response = chat.send_message(req.message)
        return {"reply": response.text}
        
    except ResourceExhausted:
        # Rate limit, the frontend will retry or show message
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
    except PermissionDenied as e:
        return JSONResponse(status_code=403, content={"detail": f"API error: {str(e)}. Check your API key and project permissions."})
    except GoogleAPIError as e:
        return JSONResponse(status_code=403, content={"detail": f"API error: {str(e)}. Check your API key and project permissions."})
    except Exception as e:
        print(f"Error in /chat: {e}")
        return JSONResponse(status_code=500, content={"detail": "Something went wrong on my end. Please retry."})

@app.post("/vision")
async def vision_endpoint(file: UploadFile = File(...), message: Optional[str] = Form("")):
    try:
        contents = await file.read()
        mime_type = file.content_type
        
        if not mime_type.startswith("image/"):
            return {"reply": "This doesn't look like an image file. Please upload a poster, character screenshot, or fan art."}
            
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-lite",
            system_instruction=SYSTEM_INSTRUCTION
        )
        
        vision_prompt = (
            "First, verify if this image is related to movies or anime. "
            "If it is NOT related (e.g., it's food, code, selfie, medical scan), reply ONLY with exactly: "
            "\"This doesn't look like a movie or anime image — try uploading a poster, character screenshot, or fan art.\"\n"
            "If it IS related to movies or anime, proceed to answer the user's message regarding the image.\n\n"
            f"User message: {message}"
        )
        
        image_part = {
            "mime_type": mime_type,
            "data": contents
        }
        
        response = model.generate_content([image_part, vision_prompt])
        return {"reply": response.text}
        
    except ResourceExhausted:
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
    except PermissionDenied as e:
        return JSONResponse(status_code=403, content={"detail": f"API error: {str(e)}. Check your API key and project permissions."})
    except GoogleAPIError as e:
        return JSONResponse(status_code=403, content={"detail": f"API error: {str(e)}. Check your API key and project permissions."})
    except Exception as e:
        print(f"Error in /vision: {e}")
        return JSONResponse(status_code=500, content={"detail": "Something went wrong on my end. Please retry."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
