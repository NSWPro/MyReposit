import logging
from aiogram import Dispatcher
from config import admins_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            text = 'Bot was started!'
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logging.exception(err)


async def on_change_ip(dp: Dispatcher, ip):
    for admin in admins_id:
        try:
            text = 'Bot was change_ip!'+ip
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logging.exception(err)