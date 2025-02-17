import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

# Insert your token here
TOKEN = "7542087081:AAEAiblB_SSkFKB2rsEUM1MuXDlhW8JW-g4"

# Set links
WEB_URL = "https://top-betting-world.webflow.io/"  # Website link
APK_URL = "https://yourdomain.com/app.apk"  # APK link
VIDEO_TUTORIAL_URL = "https://www.youtube.com/watch?v=88002J2oC_0"  # Video tutorial link

# Configure bot
logging.basicConfig(level=logging.INFO)
from aiogram.client.default import DefaultBotProperties
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
router = Router()

# Register router
router.message.filter(F.text)
dp.include_router(router)

# /start command handler
@router.message(F.text == "/start")
async def send_welcome(message: types.Message):
    print("Processing /start")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌍 Visit Website", url=WEB_URL)],
        [InlineKeyboardButton(text="📥 Download APK", url=APK_URL)],
        [InlineKeyboardButton(text="▶️ Watch Tutorial", url=VIDEO_TUTORIAL_URL)]
    ])
    
    welcome_text = (
        "<b>Welcome!</b> 👋\n\n"
        "This bot helps you register on betting platforms!\n\n"
        "<b>Select an option below:</b>"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Function to start the bot
async def main():
    print("Bot started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
