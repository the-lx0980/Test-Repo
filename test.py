from pyrogram import Client, filters
from os import environ

bot = Clinet(
    api_id = int(environ.get('ID'))
    api_hash = environ.get('HASH')
    bot_token = environ.get('TOKEN')
)



