# Created by NSW 11.11.22   rebuild 29.12.22
import datetime
from aiogram import Bot, Dispatcher, executor #, types
from config import tg_bot_token, send_id_group, send_id_admin
from myip import getip
from Mon import servstatus
import asyncio


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


async def statusregular():
    prestatus = servstatus()
    try:
      preip = getip()
    except:
        print("Ошибка определения адреса")

    await bot.send_message(send_id_group, prestatus) # To group
    #await bot.send_message(send_id_group, preip)  # To admin
    await bot.send_message(send_id_admin, preip+'   bot from here')  # to admin
    i = 0
    while True:
        await asyncio.sleep(59)
        currentstatus = servstatus()
        try:
          currentip = getip()
        except:
            print("Ошибка определения адреса")
        i += 1
        if i == 1440:
            await bot.send_message(send_id_group, currentstatus)    # To group
            i = 0
        if prestatus != currentstatus:
            await bot.send_message(send_id_group, currentstatus)    # To group
            prestatus = currentstatus
        if currentip != preip:
            #await bot.send_message(send_id_group, currentip)  # to admin
            await bot.send_message(send_id_admin, currentip+'   bot from here') # to admin
            preip = currentip

async def on_startup(_):
    print(f'Запуск бота  '+str(datetime.datetime.now()))
    await statusregular()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
