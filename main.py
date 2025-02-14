from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация клиента Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str
    style: str

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    try:
        # Формируем промпт в зависимости от выбранного стиля
        style_prompts = {
            "formal": "Переведите формально и профессионально",
            "informal": "Переведите неформально и дружелюбно",
            "business": "Переведите в стиле деловой переписки",
            "flirt": "Переведите игриво и флиртующе"
        }

        style_prompt = style_prompts.get(request.style.lower(), "formal")

        prompt = f"""
        {style_prompt} следующий текст с {request.source_language} на {request.target_language}:

        Текст: {request.text}

        Переведенный текст:
        """

        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "Вы - профессиональный переводчик."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        translated_text = completion.choices[0].message.content

        return {
            "success": True,
            "translated_text": translated_text,
            "source_language": request.source_language,
            "target_language": request.target_language,
            "style": request.style
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)