from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.filters import Filter, Command, StateFilter
    
from messages import InterfaceMessages, BirthdayMessages

birthday_router: Router = Router()
    

@birthday_router.inline_query()
async def main_handler(inline_query: InlineQuery):    
    results = []
    
    date_mes = await BirthdayMessages.check_date_mes(inline_query.query.strip())
    per_mes = await BirthdayMessages.check_per_mes(inline_query.query.strip())

    results.append(InlineQueryResultArticle(
        id="0",
        title=f"Check birthdays by date in dd.mm format",
        input_message_content=InputTextMessageContent(
            message_text=date_mes
        ),
        # thumbnail_url=currencies[cur][2]
    ))    
    
    results.append(InlineQueryResultArticle(
        id="1",
        title=f"Check birthday of the user by tg nickname",
        input_message_content=InputTextMessageContent(
            message_text=per_mes
        ),
        # thumbnail_url=currencies[cur][2]
    ))    
        
    await inline_query.answer(results, is_personal=True)
    
    