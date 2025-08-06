from telegram import Update
from telegram.ext import ContextTypes
from bot.services.weather_api import get_forecast
from bot.utils import get_text  

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("language", "en")  

    city = " ".join(context.args) if context.args else "Toronto"
    curr = get_forecast(city)
    if not curr:
        await update.message.reply_text(
            f"{get_text('city_not_found', lang)} «{city}»."
        )
        return

    temp = curr["temperature"]
    wind = curr["windspeed"]
    await update.message.reply_text(
        f"{get_text('weather', lang)} {city}:\n"
        f"{get_text('temperature', lang)} {temp}°C\n"
        f"{get_text('wind', lang)} {wind} {get_text('wind_unit', lang)}"
    )
