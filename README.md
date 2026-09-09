# 🤖 Mini AI - Простой AI Чат-Бот

Это минималистичный проект AI чат-бота на Python, использующий Claude API от Anthropic.

## ✨ Возможности

- 💬 Интерактивный диалог с AI
- 🧠 Сохранение контекста беседы
- ⚡ Быстрые ответы
- 🌐 На русском языке

## 📋 Требования

- Python 3.8+
- Anthropic API Key

## 🚀 Установка

1. **Клонируй репозиторий:**
```bash
git clone https://github.com/xumoramahmudova/mini-ai.git
cd mini-ai
```

2. **Создай виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
```

3. **Установи зависимости:**
```bash
pip install -r requirements.txt
```

4. **Создай файл `.env`:**
```bash
cp .env.example .env
```

5. **Добавь свой API ключ в `.env`:**
```
ANTHROPIC_API_KEY=your_api_key_here
```

Получить API ключ можно на https://console.anthropic.com/

## 💻 Использование

Запусти приложение:
```bash
python main.py
```

Затем просто пиши свои вопросы и общайся с AI!

Примеры:
- "Привет! Как дела?"
- "Расскажи мне анекдот"
- "Помоги мне разобраться с Python"
- "Выход" - для завершения

## 📁 Структура проекта

```
mini-ai/
├── main.py              # Главное приложение
├── requirements.txt     # Зависимости
├── .env.example        # Пример файла окружения
├── .gitignore          # Файлы для игнорирования
└── README.md           # Документация
```

## 🔧 Технологии

- **Python** - язык программирования
- **Anthropic Claude API** - AI модель
- **python-dotenv** - управление переменными окружения

## 📝 Лицензия

MIT License - свободное использование

## 🤝 Контрибьюции

Приветствуются pull requests и suggestions!

---

**Создано с ❤️ для простого AI проекта**
