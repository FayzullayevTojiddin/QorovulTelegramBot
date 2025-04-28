from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from config import Config
from handlers import router
from middlewares.authMiddleware import AuthMiddleware
from models import create_tables
import asyncio, logging, sys

bot = Bot(token=Config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()

async def main():
    create_tables()
    dp.include_router(router)
    dp.update.middleware(AuthMiddleware())
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())