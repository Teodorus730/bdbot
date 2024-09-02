from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
    
from messages import InterfaceMessages


interface_router: Router = Router()


@interface_router.message(Command("start"))
async def start_handler(msg: Message):
    mes = await InterfaceMessages.help_mes()
    await msg.answer(mes)
    
    
@interface_router.message(Command("help"))
async def help_handler(msg: Message):
    mes = await InterfaceMessages.help_mes()
    await msg.answer(mes)
    

@interface_router.message()
async def other_handler(msg: Message):
    mes = await InterfaceMessages.other_mes()
    await msg.answer(mes)
    
    
