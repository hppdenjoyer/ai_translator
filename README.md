# AI Translator

AI Translator - это веб-приложение, использующее языковую модель Groq для перевода текста с одного языка на другой. Приложение позволяет пользователям выбирать стиль перевода, включая формальный, неформальный, деловую переписку и флирт.

## Основные функции

- Перевод текста с одного языка на другой с использованием Groq API.
- Выбор стиля перевода:
  - Формальный (Formal)
  - Неформальный (Informal)
  - Бизнес-переписка (Business Email)
  - Флирт (Flirt)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/hppdenjoyer/ai-translator.git
   cd ai-translator
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Получите API ключ от Groq и добавьте его в файл `.env`:

   ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Запустите сервер:

   ```bash
   python main.py
   ```

5. Откройте файл `templates/index.html` в браузере.

## Использование

1. Выберите исходный и целевой языки перевода.
2. Введите текст, который вы хотите перевести.
3. Выберите стиль перевода.
4. Нажмите кнопку "Translate" для получения перевода.

## Технологии

- [FastAPI](https://fastapi.tiangolo.com/) - для создания бэкенда.
- [Groq](https://groq.com/) - для обработки переводов.
- [HTML/CSS/JavaScript](https://developer.mozilla.org/en-US/docs/Web) - для создания фронтенда.
