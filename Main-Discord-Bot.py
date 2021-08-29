#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import discord
import time
client = discord.Client()

import nest_asyncio
nest_asyncio.apply()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('hello'):
        await message.channel.send('Hello!')
    elif message.content == "sayı say":
        for i in range(1,11):
            await message.channel.send(i)
    elif message.content.startswith("-başlat"):
        try:
            dakikam = float(message.content.split()[1])
            await message.channel.send(f"{dakikam} dakika süreniz başladı")
            time.sleep(dakikam * 60)
            await message.channel.send(f"{dakikam} dakika süreniz doldu")
        except:
            await message.channel.send("lütfen komutu doğru kullandığınızdan emin olun")
    elif message.content.startswith('-yardım'):
        await message.channel.send('kaç dakika istiyorsanız (-başlat dakika) şeklinde botu kullanabilirsiniz')
    elif message.content.startswith('-bitir'):
        quit()
    
client.run('token') #token kısmına discord botumuzun token kısmını giriyoruz.

