from config import BOT_TOKEN
import logging
from telegram.ext import (
    ApplicationBuilder, CommandHandler, PicklePersistence, CallbackQueryHandler
)

from bot.handlers.start   import start
from bot.handlers.weather import weather
from bot.handlers.tasks   import add_task, list_tasks, done_task, stats
from bot.handlers.language import language_menu, language_button 

"""
Entry point for the Telegram bot.

This module builds and runs the Telegram bot application:
- Loads the bot token from environment via :mod:`config`.
- Enables persistence with :class:`telegram.ext.PicklePersistence` (stores user_data).
- Registers command/callback handlers for start, weather, language, and simple tasks.
- Starts long polling.

Run this module directly to start the bot.
"""

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def main():
    """
    Build and run the Telegram application.

    Steps:
        1) Create Application with token from :mod:`config`.
        2) Attach persistent storage (PicklePersistence) to keep user_data across restarts.
        3) Register all handlers (commands and callbacks).
        4) Start polling.

    This function blocks until the bot is stopped.
    """
    persistence = PicklePersistence(filepath="botdata.pkl")
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .persistence(persistence)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("language", language_menu))  
    app.add_handler(CallbackQueryHandler(language_button, pattern="^set_lang_")) 
    app.add_handler(CommandHandler("add",  add_task))   
    app.add_handler(CommandHandler("list", list_tasks)) 
    app.add_handler(CommandHandler("done", done_task))  
    app.add_handler(CommandHandler("stats", stats))     

    app.run_polling()

if __name__ == "__main__":
    main()
