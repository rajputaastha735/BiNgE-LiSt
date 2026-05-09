# Product Requirements Document — BiNgE LiSt (CineAnime Chatbot)

## Vision

BiNgE LiSt is a topic-specialized AI chatbot for movies and anime enthusiasts. It leverages Gemini to provide knowledgeable, enthusiastic, and genuinely helpful answers about films and anime — from recommendations and plot explanations to content guidance and streaming availability. The experience should feel like talking to a well-informed friend who happens to be a cinephile and anime fan, not a restrictive corporate assistant.

---

## Target User

- Casual viewers looking for something new to watch
- Anime beginners needing onboarding guidance
- Film enthusiasts seeking recommendations, analysis, or discussion
- Parents checking content suitability
- Fans wanting plot explanations, comparisons, or franchise watch orders

---

## Must-Have Features

### 1. Domain-Specialized Chat
- Chat interface powered by Gemini (`gemini-2.5-flash-lite`) with a system instruction that specializes the bot in movies and anime
- The bot **must be helpful**, not paranoid:
  - ✅ Answer general domain questions (recommendations, plot analysis, content ratings, watch orders, streaming info, production trivia)
  - ✅ Add appropriate disclaimers where relevant (e.g., "streaming availability changes by region")
  - ❌ Refuse only: serious harm, off-topic requests (coding, medical diagnoses, etc.), requests for piracy links, explicit adult content
- Conversation history maintained within a session (multi-turn context sent with each request)

### 2. Image Upload with Topic Verification
- Users can attach an image (anime screenshot, movie poster, character art, cosplay, etc.) via the `/vision` endpoint
- The bot identifies whether the image is movies/anime related before answering
- For unrelated images (food, code screenshots, selfies, medical scans), the bot politely redirects: *"This doesn't look like a movie or anime image — try uploading a poster, character screenshot, or fan art."*

### 3. Empty Message Guard
- The Send button is **disabled** when the input field is empty or contains only whitespace
- Prevents accidental or blank API calls

### 4. Markdown Rendering
- All bot responses render proper HTML Markdown (bold, italics, lists, headers)
- Gemini natively outputs `**bold**` and `*italic*` syntax — these must not appear as raw symbols in the UI
- Integration via `marked.js` (CDN)

### 5. Suggestion Chips (Empty State)
- Four tappable example questions displayed on the empty state
- Clicking a chip populates the input and sends the message automatically

### 6. Error Handling (User-Visible)
- **429 Rate Limit**: retry once after 2 seconds; if still failing, show friendly "I'm a bit busy right now — try again in a moment"
- **403 / PermissionDenied / GoogleAPIError**: show actual error message in chat (e.g., "API key is invalid or has no permissions") to aid debugging
- **Other exceptions**: log to console, show "Something went wrong — please retry"

---

## Non-Goals

- No user authentication or accounts
- No persistent chat history across sessions (in-memory only)
- No multi-language UI (English only)
- No recommendation engine beyond Gemini's generative responses
- No video playback or streaming integration
- No admin dashboard or analytics

---

## Success Criteria

| Metric | Target |
|---|---|
| Chat response latency (p50) | < 3 seconds on standard connection |
| Empty message guard | 100% — Send never fires on blank input |
| Markdown rendering | All `**`, `*`, `-` list syntax renders as HTML |
| Image topic guard | Off-topic images redirected, never answered as-if relevant |
| Error distinguishability | 429 and 403 errors show distinct, actionable messages |
| On-topic refusal rate | Zero — general domain questions answered with disclaimers, not refused |
