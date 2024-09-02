import aiosqlite
import asyncio
import datetime


async def check_bd(date: str):    
    async with aiosqlite.connect("database.sqlite") as db:
        async with db.execute('SELECT name, uname FROM users WHERE date="{}";'.format(date)) as cursor:
            rows = await cursor.fetchall()
            return rows


async def check_per(uname: str):
    async with aiosqlite.connect("database.sqlite") as db:
        async with db.execute('SELECT name, date FROM users WHERE uname="{}";'.format(uname)) as cursor:
            row = await cursor.fetchone()
            return row



async def main():
    o = await check_per("@starfedos")
    print(o)
    # a = await check_bd("30.7")
    # print(a)
    

if __name__ == "__main__":
    asyncio.run(main())
