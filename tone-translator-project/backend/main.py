import os
from typing import Literal

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
GEMINI_URL = f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent'

app = FastAPI(title='Tone Translator API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173', 'http://127.0.0.1:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

Tone = Literal['formal', 'casual', 'pirate', 'shakespeare', 'friendly', 'professional']


class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    tone: Tone


class TranslateResponse(BaseModel):
    result: str


SYSTEM_PROMPT = '''You are a rewriting assistant.
Your task is to rewrite the user's text in the requested tone.
Rules:
- Keep the original meaning.
- Keep the response in the same language as the input unless the user text clearly asks otherwise.
- Do not add explanations, notes, bullet points, or quotation marks.
- Return only the rewritten text.
'''


@app.get('/health')
def health_check():
    return {'status': 'ok'}


@app.post('/translate', response_model=TranslateResponse)
async def translate_text(payload: TranslateRequest):
    if not GEMINI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail='GEMINI_API_KEY is missing. Add it to backend/.env before starting the server.',
        )

    user_prompt = f'''Rewrite the following text in a {payload.tone} tone.\n\nText:\n{payload.text}'''

    request_body = {
        'system_instruction': {
            'parts': [{'text': SYSTEM_PROMPT}]
        },
        'contents': [
            {
                'parts': [{'text': user_prompt}]
            }
        ]
    }

    headers = {
        'x-goog-api-key': GEMINI_API_KEY,
        'Content-Type': 'application/json',
    }

    try:
        async with httpx.AsyncClient(timeout=45.0) as client:
            response = await client.post(GEMINI_URL, headers=headers, json=request_body)
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPStatusError as exc:
        detail = exc.response.text
        raise HTTPException(status_code=502, detail=f'Gemini API error: {detail}') from exc
    except httpx.RequestError as exc:
        raise HTTPException(status_code=502, detail='Could not reach Gemini API.') from exc

    try:
        result_text = data['candidates'][0]['content']['parts'][0]['text'].strip()
    except (KeyError, IndexError, TypeError):
        raise HTTPException(status_code=500, detail='Unexpected response format from Gemini API.')

    return TranslateResponse(result=result_text)
