import nextcord
import json
import os
from nextcord.ext import commands , tasks
import requests

TOKEN = ""
KEY = ""

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False
        self = self

    async def on_ready(self):

        print(f"Logged in as {client.user}!")

intents = nextcord.Intents.all()

client = Bot(command_prefix = "!", intents = intents)

@client.event
async def on_message(message):
    if message.channel.type == nextcord.ChannelType.private:
        data = requests.get(f"https://api.antisniper.net/v2/other/denick?key={KEY}&nick={message.content}").json()
        print(data)
        await message.channel.send("Request Success:",data["success"])
        if data["success"]:
            await message.channel.send("Is Nick:",data["real_nick"])
            if data["real_nick"]:
                if len(data["results"]) == 0:
                    await message.channel.send("No data found")
                else:
                    await message.channel.send(f"IGN: {data['results'][0]['ign']}\nMethod: {data['results'][0]['method']}\nPercentage: {data['results'][0]['percent']}\nFirst Detected: <t:{data['results'][0]['first_detected']}>\nLast Seen: <t:{data['results'][0]['last_seen']}>")
                

    client.run(TOKEN)
