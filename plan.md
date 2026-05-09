# Implementation Plan — BiNgE LiSt

## Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python 3.11+) |
| AI Model | `gemini-2.5-flash-lite` via `google-generativeai` Python SDK |
| Frontend | Vanilla JS — `code.html` (do NOT redesign or restyle) |
| Markdown Rendering | `marked.js` via CDN (injected into `code.html`) |
| Environment | `python-dotenv` — loads `GEMINI_API_KEY` from `.env` |
| Server | Uvicorn, port 8000 |

---

## Project Structure

```
bingelist/
├── main.py              # FastAPI app — all routes
├── code.html            # UI (from Google Stitch — do not redesign)
├── .env                 # GEMINI_API_KEY=your_key_here
├── requirements.txt     # fastapi, uvicorn, google-generativeai, python-dotenv, pillow
└── prd.md / plan.md / tasks.md
```

---

## Components (Build Order)

### 1. Environment & Dependencies
- `requirements.txt` with: `fastapi`, `uvicorn[standard]`, `google-generativeai`, `python-dotenv`, `python-multipart`, `Pillow`
- `.env` file template with `GEMINI_API_KEY=`
- `main.py` loads key via `python-dotenv` at startup; raises clear error if missing

### 2. FastAPI App Skeleton (`main.py`)
- Initialize FastAPI app
- Configure Gemini SDK: `genai.configure(api_key=...)`
- Define system instruction (movies & anime specialist, helpful not paranoid)
- Mount `code.html` served at `GET /`

### 3. `/chat` POST Endpoint
- Accepts: `{ "message": str, "history": [ {role, parts} ] }`
- Constructs a `ChatSession` with full conversation history on each call (stateless backend)
- Sends message to `gemini-2.5-flash-lite` with system instruction
- Returns: `{ "reply": str }`
- Error handling:
  - Catches `google.api_core.exceptions.ResourceExhausted` (429) → retry once after 2s
  - Catches `google.api_core.exceptions.PermissionDenied` and `google.generativeai.types.GoogleAPIError` → return actual error message
  - Catches all other exceptions → log + generic message

### 4. `/vision` POST Endpoint
- Accepts: multipart form — `file` (image) + `message` (optional text)
- Reads image bytes, encodes as base64, sends as `image/jpeg` or `image/png` inline part
- Prompt instructs model to first verify topic relevance (movies/anime), then answer
- Returns: `{ "reply": str }`
- Same error handling as `/chat`

### 5. Frontend Wiring (`code.html` modifications only)
- **Remove** all demo/placeholder content: hardcoded assistant message, hardcoded user message, any fake conversation history
- **Add** `marked.js` via CDN in `<head>`
- **Add** `<script>` block at bottom of body:
  - `conversationHistory = []` — session-scoped array
  - `sendMessage(text)` — POSTs to `/chat`, appends to history, renders response with `marked.parse()`
  - `sendImage(file, text)` — POSTs to `/vision` as FormData
  - Input event listener — enables/disables Send button based on `input.value.trim() !== ''`
  - Suggestion chip click handlers — populate input and trigger `sendMessage()`
  - Empty state hide/show logic — hides suggestion chips once first message is sent
  - Loading indicator — show typing dots while awaiting response
- **Send button guard**: button has `disabled` attribute by default; JS removes it only when input is non-empty

### 6. Markdown Rendering
- Wrap all bot bubble innerHTML assignments with `marked.parse(replyText)`
- Configure `marked` with `breaks: true` so single newlines render as `<br>`
- Sanitize output: use `marked`'s built-in options or a lightweight sanitizer to strip any `<script>` tags

### 7. Error Display in Chat
- On API errors, inject an error bubble (styled distinctly — e.g., red-tinted background) into the chat list
- 429 message: *"I'm a bit busy right now — please try again in a moment."*
- 403/PermissionDenied: *"API error: [actual error message from Gemini]. Check your API key and project permissions."*
- Generic: *"Something went wrong on my end. Please retry."*

---

## Key Constraints

- **Do not redesign `code.html`** — only wire up JS and add `marked.js`. All styling stays exactly as exported from Stitch.
- **Empty sends are blocked at the frontend** — the Send button must remain `disabled` when `input.value.trim() === ''`. This is enforced by the `input` event listener, not just on submit.
- **Gemini outputs Markdown** — every assistant bubble must go through `marked.parse()`. Skipping this causes raw `**text**` to appear literally in the UI.
- **Stateless backend** — full conversation history is sent by the frontend on every request. The backend does not store session state.
- **Free tier limits**: 15 RPM, 1000 RPD — the 429 retry logic is essential for classroom use.

---

## API Reference

- Gemini SDK docs: https://ai.google.dev/gemini-api/docs
- `gemini-2.5-flash-lite` model string: `gemini-2.5-flash-lite`
- Multimodal (vision) input: send `image` part inline as base64 with `mime_type`
