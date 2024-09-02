from utils.validations import check_date_val, check_per_val
from utils.database import check_bd, check_per

import datetime


class InterfaceMessages:
    async def help_mes():
        return "its help message"
    
    async def other_mes():
        return "its other message"
    
    
class BirthdayMessages:
    async def check_date_mes(date: str):
        date_val = check_date_val(date)
        if not date_val:
            return "Please use dd.mm format"
        
        rows = await check_bd(date_val)
        
        d, m = map(int, date_val.split("."))
        day = datetime.date(month=m, day=d, year=2024)
    
        if not rows:
            return f"No birthdays at {day.strftime("%d of %B")}. Chill"
    
        return f"At {day.strftime("%d of %B")} some good people were born:\n{"\n".join(map(lambda x: ' '.join(x), rows))}\nHappy birthday!"
        
        
    async def check_per_mes(uname: str):
        per_val = check_per_val(uname)
        if not per_val:
            return "Write tg nickname wich starts with @"
        
        row = await check_per(per_val)
                        
        if not row:
            return f"There is no {uname} in database"
            
        d, m = map(int, str(row[1]).split("."))
        return f"The guy {uname} {row[0]} was born at {d} of {datetime.date(day=d, month=m, year=2024).strftime("%B")}"
        
    