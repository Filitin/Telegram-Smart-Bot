from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.utils import get_text, show_main_menu

async def language_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Show an inline keyboard to choose the interface language.

    Presents three options (RU/EN/UK) with callback data in the format
    `set_lang_<code>`. Works both from a command message and from a callback.

    Args:
        update: Telegram update (command or callback).
        context: Callback context.
    """
    keyboard = [
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data="set_lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en"),
            InlineKeyboardButton("🇺🇦 Українська", callback_data="set_lang_uk"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(
            "Выберите язык / Choose language:", reply_markup=reply_markup
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            "Выберите язык / Choose language:", reply_markup=reply_markup
        )

async def language_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    andle language selection callbacks and refresh the main menu.

    Extracts the language code from the callback data, stores it in
    `context.user_data["language"]`, confirms the selection to the user, and
    then renders the main menu in the new language.

    Args:
        update: Telegram update with `callback_query`.
        context: Callback context.
    """
    query = update.callback_query
    await query.answer()

    lang_code = query.data.split("_")[-1]
    context.user_data["language"] = lang_code

    await query.edit_message_text(text=get_text("language_selected", lang_code))
    await show_main_menu(update, context)
