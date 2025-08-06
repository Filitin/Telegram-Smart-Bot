from dotenv import load_dotenv
from os import getenv

load_dotenv()
"""
Configuration loader for environment variables.

Loads environment variables from a local `.env` file using `python-dotenv`
and exposes them as module-level constants.

Attributes:
    BOT_TOKEN (str | None): Telegram bot token read from the `BOT_TOKEN` env var.
"""
BOT_TOKEN = getenv("BOT_TOKEN")