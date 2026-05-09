# Build Tasks — BiNgE LiSt

## Execution Order

---

**Task 1 — Create project structure and `requirements.txt`**
Create the `bingelist/` project folder. Add `requirements.txt` containing: `fastapi`, `uvicorn[standard]`, `google-generativeai`, `python-dotenv`, `python-multipart`, `Pillow`.

---

**Task 2 — Load `GEMINI_API_KEY` from a `.env` file**
Create a `.env` file in the project root with the line `GEMINI_API_KEY=your_key_here`. In `main.py`, use `python-dotenv` (`load_dotenv()`) to load the key at startup, and raise a clear `RuntimeError` if the variable is missing or empty.

---

**Task 3 — Initialize FastAPI app and configure Gemini SDK**
In `main.py`, initialize the FastAPI app and call `genai.configure(api_key=GEMINI_API_KEY)`. Define the system instruction string for the movies & anime specialist: helpful, not paranoid — answers domain questions with disclaimers, refuses only serious harm, off-topic requests, piracy links, and explicit adult content.

---

**Task 4 — Serve `code.html` at `GET /`**
Add a route `GET /` that reads and returns `code.html` as an HTML response using `FileResponse`. This makes the app self-contained — no separate static file server needed.

---

**Task 5 — Build `/chat` POST endpoint with error handling**
Accept `{ "message": str, "history": list }`. Reconstruct the chat session from history on each call (stateless), send the user message to `gemini-2.5-flash-lite`, and return `{ "reply": str }`. Handle errors distinctly: catch `ResourceExhausted` (429) with one 2-second retry then a friendly busy message; catch `PermissionDenied` / `GoogleAPIError` and return the actual error text so students can debug bad API keys; catch all other exceptions with a generic retry message.

---

**Task 6 — Build `/vision` POST endpoint**
Accept a multipart form with `file` (image upload) and optional `message` (text). Read the image bytes, detect MIME type, encode as base64, and send to `gemini-2.5-flash-lite` as an inline image part alongside a prompt that first asks the model to verify the image is movies/anime related before responding. Apply the same error handling as Task 5.

---

**Task 7 — Remove all demo/placeholder data from `code.html`**
Delete the two hidden example message bubbles (the hardcoded assistant and user messages inside the `hidden` chat area div) from `code.html`. The chat must start completely empty — no fake conversation history, no sample replies, no placeholder responses.

---

**Task 8 — Add `marked.js` and wire up Markdown rendering**
Add `<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>` to `code.html`'s `<head>`. Ensure every assistant message bubble's `innerHTML` is set using `marked.parse(replyText, { breaks: true })` so that Gemini's `**bold**`, `*italic*`, and list syntax render as proper HTML — never as raw symbols.

---

**Task 9 — Implement empty-send guard on the Send button**
Attach an `input` event listener to the text field in `code.html`. When `input.value.trim() === ''`, set the Send button to `disabled` with `opacity-[0.38]` and `cursor-not-allowed` classes (matching the existing Stitch design). Remove `disabled` and restore full opacity only when the field contains non-whitespace text. The button must start in the disabled state on page load.

---

**Task 10 — Wire up `sendMessage()` to `/chat` and manage conversation history**
Implement `sendMessage(text)` in `code.html`'s script: append the user bubble to the DOM, push `{ role: "user", parts: [{ text }] }` to `conversationHistory`, POST `{ message: text, history: conversationHistory }` to `/chat`, then append the assistant bubble using `marked.parse()` on the reply and push the assistant turn to history.

---

**Task 11 — Wire up image upload to `/vision`**
Attach a `change` event listener to the attach-file button's hidden `<input type="file">`. On file selection, POST the image and any current input text as `FormData` to `/vision`. Render the assistant reply with `marked.parse()` the same way as text chat.

---

**Task 12 — Implement suggestion chip click handlers and empty state hide logic**
Add click handlers to all four suggestion chip buttons so that clicking one populates the text input with the chip's label and triggers `sendMessage()` immediately. After the first message is sent, hide the empty-state container (the icon, heading, and chips) and show the scrollable chat area.

---

**Task 13 — Add loading/typing indicator**
While awaiting a response from `/chat` or `/vision`, inject a temporary "typing" bubble (three animated dots) into the chat list and disable the Send button. Remove the typing bubble and re-enable the Send button once the response arrives or an error occurs.

---

**Task 14 — Final check: run on port 8000 and verify all behaviors**
Start the server with `uvicorn main:app --port 8000 --reload`. Verify: (1) empty Send button is disabled on load, (2) suggestion chips send messages, (3) Markdown bold/italic renders correctly, (4) image upload triggers `/vision`, (5) a wrong API key shows a PermissionDenied message in chat (not a generic busy message), (6) no hardcoded demo messages appear on load.
