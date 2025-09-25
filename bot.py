from pyrogram import Client, filters
from os import getenv

app_id = int(getenv('API_ID'))
api_hash = getenv('API_HASH', '')
bot_token = getenv('BOT_TOKEN', '') 

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
