import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

# Встав свій токен тут
TOKEN = "7542087081:AAEAiblB_SSkFKB2rsEUM1MuXDlhW8JW-g4"

# Вказуємо посилання
WEB_URL = "https://top-betting-world.webflow.io/"  # Посилання на сайт
APK_URL = "https://yourdomain.com/app.apk"  # Посилання на APK
VIDEO_TUTORIAL_URL = "https://www.youtube.com/watch?v=88002J2oC_0"  # Посилання на відео туторіал

# Налаштовуємо бота
logging.basicConfig(level=logging.INFO)
from aiogram.client.default import DefaultBotProperties
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
router = Router()

# Реєструємо роутер
router.message.filter(F.text)
dp.include_router(router)

# Обробник команди /start
@router.message(F.text == "/start")
async def send_welcome(message: types.Message):
    print("Обробляємо /start")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌍 Перейти на сайт", url=WEB_URL),
         InlineKeyboardButton(text="📥 Завантажити APK", url=APK_URL),
         InlineKeyboardButton(text="▶️ Відео туторіал", url=VIDEO_TUTORIAL_URL)]
    ])
    
    welcome_text = (
        "<b>Привіт!</b> 👋\n\n"
        "Цей бот допоможе тобі пройти реєстрацію на букмекерських сайтах!\n\n"
        "<b>Оберіть одну з опцій нижче:</b>"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Функція для запуску бота
async def main():
    print("Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
