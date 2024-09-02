import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import load_config
from handlers.interface import interface_router
from handlers.birthday import birthday_router

from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO
    )
    
    logger.info("*** Starting bot ***")
    config = load_config(".env")
            
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(birthday_router)    
    dp.include_router(interface_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        print(e)
        logging.ERROR(e)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("*** Shutting down ***")
