# Smart Assistant Telegram Bot

A multilingual personal assistant bot for Telegram, written in Python 3.x using the `python‑telegram‑bot` asyncio framework.

## ✨ Features

- **Language selector** – Inline keyboard lets users switch between English, Russian and Ukrainian.
- **Weather forecast** – `/weather [city]` returns the current temperature and wind speed using the **Open‑Meteo** public API.
- **Task list** – `/add`, `/list`, `/done`, `/stats` manage a per‑user to‑do list stored in memory (compatible with `PicklePersistence`).
- **Main menu** – Localised command cheat‑sheet presented by `/start` and after every language change.
- **Async handlers** – Built on top of `python‑telegram‑bot>=20`, fully asyncio‑ready.
- **Simple i18n** – Plain‑dict translation table in `bot/translations.py` makes adding new languages trivial.

## 🚀 Quick start

### Prerequisites

- Python ≥ 3.11
- A Telegram Bot API token

### Installation

```bash
# 1. Get the code
$ git clone https://github.com/yourname/smart-assistant-bot.git
$ cd smart-assistant-bot

# 2. Create & activate virtual env (optional but recommended)
$ python -m venv .venv
$ source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Configure secrets
$ cp .env.example .env        # then edit .env and set BOT_TOKEN=<your token>
```

### Run locally

```bash
python -m bot   # or python bot/main.py once you add an entry‑point
```

The bot will start polling. Talk to it on Telegram to verify the `/start` menu.

## ⚙️ Commands

| Command           | Description                                |
| ----------------- | ------------------------------------------ |
| `/start`          | Show the main menu and language picker     |
| `/language`       | Open inline language selection menu        |
| `/weather [city]` | Show current weather (defaults to Toronto) |
| `/add <task>`     | Add a new task                             |
| `/list`           | List all tasks                             |
| `/done <number>`  | Mark the numbered task as done             |
| `/stats`          | Show total and completed task counters     |

All commands are also listed in the localised main menu.

## 🗂 Project structure

```
bot/
  handlers/
    language.py      # /language callbacks
    tasks.py         # /add, /list, /done, /stats
    weather.py       # /weather
  services/
    weather_api.py   # Open‑Meteo client
  translations.py    # RU/EN/UK messages
  utils.py           # helpers: i18n lookup, show_main_menu()
start.py             # handler wiring (imported by main)
```

## 🛠 Configuration

- **Environment vars** – `BOT_TOKEN` is **required**; everything else is optional.
- **Translations** – Add or edit keys directly in `bot/translations.py`.

## 🗺 Roadmap

- Replace blocking `requests` with `aiohttp` for non‑blocking HTTP I/O.
- Persist tasks to SQLite (`aiosqlite`) or via `PicklePersistence`.
- Add unit tests (`pytest`, `pytest‑telegram‑bot`).
- Docker container & GitHub Actions CI pipeline.

## 🤝 Contributing

1. Fork the repo & create your branch (`git checkout -b feature/foo`)
2. Commit your changes (`git commit -am 'Add some foo'`)
3. Push to the branch (`git push origin feature/foo`)
4. Create a new Pull Request

Please open an issue first if you plan major API changes.