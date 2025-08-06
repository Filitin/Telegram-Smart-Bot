from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.language import language_menu
from bot.utils import show_main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your Smart Assistant.")
    await language_menu(update, context) 