# Tone Translator

A simple **Level 1** LLM project:
- **Frontend:** React (Vite)
- **Backend:** FastAPI
- **LLM integration:** Gemini API
- **Communication:** HTTP POST from frontend to backend

The app rewrites user text in a selected tone. This matches the Level 1 requirement because it is a **single-turn application**: one prompt in, one response out.

## Architecture Overview
The application follows a simple client-server architecture:

React frontend → FastAPI backend → Gemini API

The React frontend sends user input (text and tone) to the FastAPI backend via an HTTP POST request.

The backend constructs a prompt and sends it to the Gemini API.

The Gemini API processes the request and returns generated text, which is then sent back to the frontend and displayed to the user.

## Technical Choices
React (Vite) was used for the frontend because it is fast, simple, and well-suited for building interactive user interfaces.

FastAPI was chosen for the backend because it is lightweight, easy to use, and supports asynchronous requests.

httpx is used for making asynchronous HTTP requests to the Gemini API.

Pydantic is used for request validation to ensure correct input data.

The Gemini API was used as the LLM provider because it offers a free tier and simple integration.

## Known limitations
This application is a simple prototype and has several limitations:

There is no input validation on the frontend beyond basic checks.

The application does not handle conversation history or multi-turn interactions.

Error handling is basic and not user-friendly.

The API key is stored locally and not secured for production use.

The UI is minimal and not optimized for mobile devices.

For production use, authentication, better error handling, and input sanitization would be required.

## AI Assistant 

AI tools were used during development mainly to assist with understanding concepts, debugging, and documentation.

ChatGPT was used to explain implementation details, help troubleshoot frontend-backend communication issues, and assist in writing parts of the README.

AI assistance was used as a support tool during development, while the core logic, structure, and implementation decisions were done independently.

## Features
- Paste or write text
- Choose a tone
- Send request from React frontend to FastAPI backend
- Backend calls Gemini API once and returns the rewritten text
- Runs locally from the repository

## Project structure

```text
tone-translator-project/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── .gitignore
└── README.md
```

## 1. Get a Gemini API key
Create a Gemini API key in Google AI Studio.

## 2. Backend setup
Open a terminal in the `backend` folder:

### Windows PowerShell
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```


Start the backend:

```bash
uvicorn main:app --reload
```

Backend runs at:
`http://localhost:8000`

Health check:
`http://localhost:8000/health`

## 3. Frontend setup
Open another terminal in the `frontend` folder:

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
`http://localhost:5173`

## 4. How to use
1. Write or paste text into the textbox.
2. Choose a tone.
3. Click **Translate**.
4. The rewritten text appears below.

## 5. Why this is Level 1
This project fits **Level 1** because:
- it uses **one LLM request** per action
- there is **no conversation memory**
- there is **no retrieval / RAG**
- there is **no tool use**
- it is a simple wrapper around a single API call with prompt design
