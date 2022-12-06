from email import message
from mailbox import Babyl
from smtplib import SMTPSenderRefused
from telethon import TelegramClient, events, sync
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.client.telegramclient import TelegramClient
import os
import random

api_id = 1225523
api_hash = 'ec0ae6e668e4eaa669c536acf13c9f59'
bot_token = '5915223655:AAF924-X46JlyKAf1xv6Q2dHUR3zHQYp_c4'


client = TelegramClient('salam', api_id, api_hash)
client.start(bot_token=bot_token)

nurlanmsg = ["salam admin məllim","salam şəfşələy","səni kim çağırdı ala","ehh yenə gədidə","salam","sağol","??","salam qaqaş","nəyə gəlmisən?"]
babasmsg = ["salam qaqaş","salam","salam məllim","sağol"]







@client.on(events.NewMessage(incoming=True, pattern='^salam'))
async def handler(event):
    nurlana = random.choice(nurlanmsg)
    babasa = random.choice(babasmsg)

    sender = await event.get_sender()
    
    if sender.id == 1339412165:
       await event.reply(babasa)
    elif sender.id == 1464910930:
        await event.reply(nurlana)
    else:
        pass

client.run_until_disconnected()

