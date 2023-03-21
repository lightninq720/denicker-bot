import nextcord
import json
import os
from cogs.tickets import TicketsView, TicketManagementView, FAQView
from cogs.rolemenu import RoleMenuView
from nextcord.ext import commands , tasks
import requests

users = [710044207670231061, 434603846120112130, 326065974950363136]

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
    if message.author.id in usersn and message.channel.type == nextcord.ChannelType.private:
        data = requests.get(f"https://api.antisniper.net/v2/convert/hypixel?key=bc3ba89b-2a57-46d3-af90-733cc3b439a5&player={message}").json()
        await message.channel.send(data["success"])
        if data["success"]:
            await interaction.channel.send(data["real_nick"])
            if data["real_nick"]:
                await message.channel.send(f"IGN: {data['results'][0]['ign']}\nMethod: {data['results'][0]['method']}\nPercentage: {data['results'][0]['percentage']}\nFirst Detected: <t:{data['results'][0]['first_detected']}>\nLast Seen: <t:{data['results'][0]['last_seen']}>")
                

client.run("MTA4Nzg1NjkzMTEzMTExMzU0Mg.GZadzx.L1v4f52mTRzd271MWtX1pecre4B245eGnjY6oc")
