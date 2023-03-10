#This token is confidential information and may not be shared with anyone else
import os
TOKEN = os.environ['TOKEN']

import discord 
from discord import app_commands

#Variables
intents = discord.Intents.all()
client = client=discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)
masteroogwgaywebhook = os.environ['MASTEROOGWGAY']

#Testers
beta_testers = ["612522818294251522"]
