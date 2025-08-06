from bot.translations import translations
from telegram import Update
from telegram.ext import ContextTypes

def get_text(key: str, lang: str = "en") -> str:
    """
    Return a localized text for the given key and language.

    If the `key` or the language entry is missing, the function returns the key
    itself as a safe fallback (helps detect missing translations at runtime).

    Args:
        key: Translation key, e.g. `"menu_start"`.
        lang: Language code (`"en"`, `"ru"`, `"uk"`).

    Returns:
        Localized string or the original key when not found.
    """
    return translations.get(key, {}).get(lang, key)

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send the main command menu in the user's current language.

    Reads the language from `context.user_data["language"]` (defaults to `"en"`)
    and composes a multi-line message from menu-related translation keys.

    Args:
        update: Telegram update.
        context: Callback context with `user_data`.

    Side Effects:
        Sends a message either via `update.callback_query.message` or
        `update.message`, depending on the trigger.
    """
    lang = context.user_data.get("language", "en")
    commands = [
        get_text("menu_start", lang),
        get_text("menu_weather", lang),
        get_text("menu_add", lang),
        get_text("menu_list", lang),
        get_text("menu_done", lang),
        get_text("menu_stats", lang),
        get_text("menu_language", lang),
    ]
    menu_text = f"{get_text('main_menu_title', lang)}\n\n" + "\n".join(commands)

   
    if update.callback_query:
        await update.callback_query.message.reply_text(menu_text)
    else:
        await update.message.reply_text(menu_text)