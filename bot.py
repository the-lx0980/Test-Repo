from pyrogram import Client, filters
from os import environ

app_id = int(environ.get('ID'))
api_hash = environ.get('HASH')
bot_token = environ.get('TOKEN')

bot = Client(    
    name='test-bot',
    api_id=app_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@bot.on_message(filters.command('start'))
async def start(bot, message):
    await message.reply('Alive! ------->  Zinda hai!!!!')

print('Bot Started!')
bot.run()
