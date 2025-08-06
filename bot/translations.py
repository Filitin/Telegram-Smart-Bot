translations = {
"""
Human-readable text strings used for localization.

This module defines the `translations` dictionary with keys for UI messages.
Each key maps to a dict of language codes (`"en"`, `"ru"`, `"uk"`).

Notes:
    - Add missing keys here to prevent fallback to the raw key.
    - Keep messages short; they are displayed in chat or inline keyboards.
"""
    "start": {
        "ru": "Привет! Я твой Smart Assistant.",
        "en": "Hello! I am your Smart Assistant.",
        "uk": "Привіт! Я твій Smart Assistant."
    },
    "weather": {
        "ru": "Погода в",
        "en": "Weather in",
        "uk": "Погода у"
    },
    "temperature": {
        "ru": "Температура:",
        "en": "Temperature:",
        "uk": "Температура:"
    },
    "wind": {
        "ru": "Ветер:",
        "en": "Wind:",
        "uk": "Вітер:"
    },

    "wind_unit": {
        "ru": "км/ч",
        "en": "km/h",
        "uk": "км/год"
    },

    "city_not_found": {
        "ru": "Не нашел город",
        "en": "City not found",
        "uk": "Не знайшов місто"
    },
    "language_selected": {
        "ru": "Вы выбрали русский язык.",
        "en": "You have selected English.",
        "uk": "Ви обрали українську мову."
    },
    "choose_language": {
        "ru": "Выберите язык: /language ru, /language en, /language uk",
        "en": "Choose a language: /language ru, /language en, /language uk",
        "uk": "Оберіть мову: /language ru, /language en, /language uk"
    },
    "add_usage": {
        "ru": "Используй: /add купить хлеб",
        "en": "Use: /add buy bread",
        "uk": "Використовуйте: /add купити хліб"
    },
    "task_added": {
        "ru": "Задача добавлена!",
        "en": "Task added!",
        "uk": "Завдання додано!"
    },
    "no_tasks": {
        "ru": "Нет задач.",
        "en": "No tasks.",
        "uk": "Немає завдань."
    },
    "main_menu_title": {
        "ru": "Я могу помочь тебе с такими командами:",
        "en": "I can help you with these commands:",
        "uk": "Я можу допомогти тобі з цими командами:"
    },
    "menu_start": {
        "ru": "/start - Перезапустить бота и выбрать язык",
        "en": "/start - Restart the bot and select language",
        "uk": "/start - Перезапустити бота та обрати мову"
    },
    "menu_weather": {
        "ru": "/weather [город] - Узнать погоду",
        "en": "/weather [city] - Get the weather",
        "uk": "/weather [місто] - Дізнатися погоду"
    },
    "menu_add": {
        "ru": "/add [задача] - Добавить задачу",
        "en": "/add [task] - Add a task",
        "uk": "/add [завдання] - Додати завдання"
    },
    "menu_list": {
        "ru": "/list - Показать список задач",
        "en": "/list - Show task list",
        "uk": "/list - Показати список завдань"
    },
    "menu_done": {
        "ru": "/done [номер] - Отметить задачу выполненной",
        "en": "/done [number] - Mark task as done",
        "uk": "/done [номер] - Відзначити завдання виконаним"
    },
    "menu_stats": {
        "ru": "/stats - Показать статистику",
        "en": "/stats - Show statistics",
        "uk": "/stats - Показати статистику"
    },
    "menu_language": {
        "ru": "/language - Сменить язык",
        "en": "/language - Change language",
        "uk": "/language - Змінити мову"
    }
}