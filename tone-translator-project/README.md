# Tone Translator

A simple **Level 1** LLM project:
- **Frontend:** React (Vite)
- **Backend:** FastAPI
- **LLM integration:** Gemini API
- **Communication:** HTTP POST from frontend to backend

The app rewrites user text in a selected tone. This matches the Level 1 requirement because it is a **single-turn application**: one prompt in, one response out.

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

