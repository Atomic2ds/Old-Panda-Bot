import os

#------------ Bot Configuration ------------

#Below is some configuration for the Bot including the token, imports,
#Bot login and MySQL databases

#------------ All Imports ------------

#Data Imports
import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio
import giphy_client
from giphy_client.rest import ApiException
from discord import Webhook
import aiohttp
from typing import List
from discord.app_commands import Choice
from discord import ui
import colorama
from colorama import Fore
from generator import catimages
from generator import dogimages
from generator import number_list
from webserver import web_server
from replit import db
from discord import Webhook
import time
import traceback

#Configuration
import config
from config import TOKEN
from config import intents
from config import client
from config import tree
from config import masteroogwgaywebhook

#------------ Bot Triggers and Slash Commands ------------

#Below is all the code for Triggers and slash commands, all Triggers and
#slash commands are named with a comment above all the commands

#Update: I have removed all triggers and moved exclusively to slash commands

#------------ Member Event Messages Lunar Lounge ------------

#These are messages that are sent when a user joins
#or leaves the Lunar Lounge


@client.event
async def on_member_join(member):
  pass


#------------ Block Spam ------------


@client.event
async def on_message(msg):

  #------------ Master oogwgay ------------

  prefix = "master "
  if msg.content.lower() == ("master help"):
    embedVar = discord.Embed(
      description=
      "```master help economy``````master help triggers``````master help games``````master help modules``````master help leveling```",
      colour=0xffb500,
      title="Master oogwgay Help")
    embedVar.set_author(name=msg.guild.name)
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await webhook.send(embed=embedVar)
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")

  #Test Master oogwgay webhook
  if msg.content.lower() == "master test":
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await msg.reply("I sent a message to the Master oogwgay webhook")
        await webhook.send("Your webhook test worked!")
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")

  #Ping Message
  if msg.content.lower() == f"{prefix}ping":
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await webhook.send("Pong!")
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")

  #Help Command Triggers
  if msg.content.lower() == "master help triggers" or msg.content.lower(
  ) == f"{prefix}help triggers":
    await msg.reply("Not ready for use")

  if msg.content.lower() == "master help economy" or msg.content.lower(
  ) == f"{prefix}help economy":
    embedVar = discord.Embed(
      description=
      f"```{prefix}balance``````{prefix}beg``````master jobs``````master job progress``````master job set <name>```",
      title="Oogwgay Economy",
      colour=0xffb500)
    embedVar.set_author(name=msg.guild.name)
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await webhook.send(embed=embedVar)
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")

  if msg.content.lower() == f"master balance" or msg.content.lower(
  ) == "master bal":
    db_keys = db.keys()
    if f"{msg.author.id}-account_balance" in db_keys:
      account_balance = db[f"{msg.author.id}-account_balance"]
      embedVar = discord.Embed(
        description=f"You have ``${account_balance}`` in your account",
        title="Account Balance",
        colour=0xffb500)
      embedVar.set_author(name=msg.guild.name)
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(embed=embedVar)
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")
    else:
      embedVar = discord.Embed(description="You have ``$50`` in your account",
                               title="Account Balance",
                               colour=0xffb500)
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(embed=embedVar)
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")

  if msg.content.lower() == "master beg":
    db_keys = db.keys()
    if f"{msg.author.id}-account_balance" in db_keys:
      account_balance = db[f"{msg.author.id}-account_balance"]
    else:
      account_balance = "50"
    money_earned_int = int(random.choice(number_list))
    balance_int = int(account_balance)
    money_earned = str(money_earned_int)
    finished_balance = balance_int + money_earned_int
    saved_balance = str(finished_balance)
    db[f"{msg.author.id}-account_balance"] = saved_balance
    embedVar = discord.Embed(
      title="Oogwgay Bank",
      colour=0xffb500,
      description=f"You poor thing, take ``${money_earned}``")
    embedVar.set_author(name=msg.guild.name)
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await webhook.send(embed=embedVar)
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")

  if msg.content.lower() == "master help games":
    embedVar = discord.Embed(description="```master play hangman```",
                             title="Oogwgay Games",
                             colour=0xffb500)
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await webhook.send(embed=embedVar)
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")

  if msg.content.lower() == "master jobs":
    embedVar = discord.Embed(
      title="Oogwgay Jobs",
      description="```Programmer``````Twitch Mod``````Reddit Mod```",
      colour=0xffb500)
    embedVar.set_footer(text="master job set <job_name>")
    embedVar.set_author(name=msg.guild.name)
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await webhook.send(embed=embedVar)
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")

  if msg.content.lower() == "master job set programmer":
    db_keys = db.keys()
    if f"{msg.author.id}-job" in db_keys:
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(
            "You must quit your current job before starting a new job ``master job quit``"
          )
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")
    else:
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(
            "Congrats! You have started working as a Programmer, use ``master work`` daily to keep your job"
          )
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")
      db[f"{msg.author.id}-job"] = "programmer"
  if msg.content.lower() == "master job set twitch mod":
    db_keys = db.keys()
    if f"{msg.author.id}-job" in db_keys:
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(
            "You must quit your current job before starting a new job ``master job quit``"
          )
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")
    else:
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(
            "Congrats! You have started working as a Twitch Mod, use ``master work`` daily to keep your job"
          )
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")
      db[f"{msg.author.id}-job"] = "twitch_mod"
  if msg.content.lower() == "master job set reddit mod":
    db_keys = db.keys()
    if f"{msg.author.id}-job" in db_keys:
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(
            "You must quit your current job before starting a new job ``master job quit``"
          )
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")
    else:
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
        if msg.channel == client.get_channel(1052895253524402226):
          await webhook.send(
            "Congrats! You have started working as a Reddit Mod, use ``master work`` daily to keep your job"
          )
        else:
          await msg.reply(
            "This command is only available in <#1052895253524402226>")
      db[f"{msg.author.id}-job"] = "reddit_mod"

  if msg.content.lower() == "master job quit":
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(masteroogwgaywebhook, session=session)
      if msg.channel == client.get_channel(1052895253524402226):
        await webhook.send("Successfully quit your current job")
      else:
        await msg.reply(
          "This command is only available in <#1052895253524402226>")
    del db[f"{msg.author.id}-job"]

  if msg.content.lower() == "master":
    await msg.reply("Put something after instead of wasting my time")

  if msg.content.lower() == "#fuckmee6":
    await msg.reply("W")

#------------ Ghost Lunar ------------

#Hello trigger for Ghost Lunar
  if msg.content.lower().startswith(
      "hello lunar") or msg.content.lower().startswith("hi lunar"):
    async with aiohttp.ClientSession() as session:
      user = msg.author
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      await webhook.send(f"Hello <@!{user.id}>", username="Ghost Lunar")

  #Triggers for Ghost Lunar
  if msg.content.lower().startswith("ghost triggers"):
    async with aiohttp.ClientSession() as session:
      embedVar = discord.Embed(
        title="Lunar Triggers",
        description=
        "``hi lunar``\n``hello lunar``\n``lunar entertain me``\n``entertain me lunar`` ``lunar go fuck yourself`` ``go fuck yourself lunar``"
      )
      embedVar.set_footer(text="Lunar Lounge")
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      await webhook.send(embed=embedVar)

  #Commands for Ghost Lunar
  if msg.content.lower().startswith("ghost cmds"):
    async with aiohttp.ClientSession() as session:
      embedVar = discord.Embed(
        title="Lunar Commands",
        description=
        "``ghost cmds``\n``ghost triggers``\n``ghost about``\n``ghost ping``")
      embedVar.set_footer(text="Lunar Lounge")
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      await webhook.send(embed=embedVar)

  #Ghost Lunar Ping
  if msg.content.lower().startswith("ghost ping"):
    async with aiohttp.ClientSession() as session:
      user = msg.author
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      await webhook.send(":ping_pong: Pong!")

  #Go fuck yourself lunar trigger
  if msg.content.lower().startswith(
      "go fuck yourself lunar") or msg.content.lower().startswith(
        "lunar go fuck yourself"):
    async with aiohttp.ClientSession() as session:
      user = msg.author
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      await webhook.send(f"stfu bitch")

  #Test Command
  if msg.content.lower().startswith(
      "commands lunar") or msg.content.lower().startswith("lunar commands"):
    async with aiohttp.ClientSession() as session:
      user = msg.author
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      await webhook.send(view=helpmenuview())

  #@everyone trigger
  if "@everyone" in msg.content.lower():
    if msg.author != client.user:
      if msg.guild.id == 1054681613138673674 or msg.guild.id == 998548528160837653:
        embedVar = discord.Embed(
          description="@everyone is disabled by default", colour=0x4a4a4a)
        await msg.channel.send(embed=embedVar)

  #OMDs trigger
  if "omds" in msg.content.lower():
    if msg.author != client.user:
      if msg.author.bot == False:
        if msg.guild.id == 1054681613138673674 or msg.guild.id == 998548528160837653:
          omds_list = [
            "omds = oh my dicks small", "omds = oh my dads sexy",
            "omds = oh my dicks sexy", "omds = oh my dicks sticky",
            "omds = oh my dicks salty"
          ]
          omds_response = random.choice(omds_list)
          await msg.channel.send(omds_response)

  #Goodnight Command
  if msg.content.lower() == "goodnight lunar" or msg.content.lower(
  ) == "gn lunar":
    if msg.author != client.user:
      async with aiohttp.ClientSession() as session:
        user = msg.author
        goodnight_messages = [
          f"(╯°□°)╯︵ ┻━┻ Goodnight <@{user.id}> (╯°□°)╯︵ ┻━┻",
          f"¯\_(ツ)_/¯ Goodnight <@{user.id}> ¯\_(ツ)_/¯",
          f"┬─┬ノ( º _ ºノ) Goodnight <@{user.id}> ┬─┬ノ( º _ ºノ)"
        ]
        goodnight_response = random.choice(goodnight_messages)
        webhook = Webhook.from_url(
          'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
          session=session)
        await webhook.send(goodnight_response)


#----------- Info Embeds ------------

  if msg.content.lower() == "%rules":
    embedVar = discord.Embed(title="Server Wide Rules", colour=0x2f3136)
    embedVar.set_author(name="Lunar Lounge・Important Information 🌏")
    embedVar.set_footer(text="Lunar Lounge")
    embedVar.add_field(
      name="Rule List",
      value=
      " ```1. No Spamming, posting ip grabber links or self advertising```  ```2. No being racist (unless you're joking around)```  ```3. Don't post ip grabber links, personal information or anything else that could be used to deal harm to others``` ",
      inline=False)
    embedVar.add_field(
      name="Whats the point of having rules?",
      value=
      "```Lunar Lounge has rules in place simply so that the server doesn't become a giant warzone, thats about it. However, our rules are pretty basic and self explanatory ```",
      inline=False)
    if msg.author == client.get_user(612522818294251522):
      await msg.channel.send(embed=embedVar)
    else:
      await msg.reply("This command is not available")

  if msg.content.lower() == "%info":
    embedVar = discord.Embed(title="Server Wide Rules", colour=0x2f3136)
    embedVar.set_author(name="Lunar Lounge・Information 🌌")
    embedVar.set_footer(text="Lunar Lounge")
    embedVar.add_field(
      name="How do I earn level roles?",
      value=
      "Our levelling system is handled by <@437808476106784770>, the way it works is basically, whenever you send a message to the server you get some experience. As you get more experience, you level up (Check your rank in <#1000686516558897162> by doing /rank)",
      inline=False)
    embedVar.add_field(
      name=f"What do level roles actually do?",
      value=
      "Here is the list of perks that you get from leveling up!\n\n<@&1010119564916437032> ``=`` Add new Reactions to messages\n<@&1010119709036904508> ``=`` Change your nickname\n<@&1010119773574680628> ``=`` Use external emojis\n<@&1010119886246252564> ``=`` Use external stickers\n<@&1010119994362835014> ``=`` Create public and private threads\n<@&1010120094585737296> ``=`` Use TTS and @everyone",
      inline=False)
    embedVar.add_field(
      name="How do I know when I level up?",
      value=
      "When you level up in the server there will be a message sent in the same channel as you from <@437808476106784770> saying that you have leveled up!",
      inline=False)
    embedVar.add_field(
      name="Level Role List",
      value=
      "``Level 5`` ``=`` <@&1010119564916437032>\n``Level 10`` ``=`` <@&1010119709036904508>``\nLevel 20`` ``=`` <@&1010119773574680628>"
    )
    embedVar.add_field(
      name="",
      value=
      "``Level 30`` ``=`` <@&1010119886246252564>``\nLevel 40`` ``=`` <@&1010119994362835014>``\nLevel 50`` ``=`` <@&1010120094585737296>"
    )
    if msg.author == client.get_user(612522818294251522):
      await msg.channel.send(embed=embedVar)
    else:
      await msg.reply("This command is not available")

  if msg.content.lower() == "%lfgroles":
    if msg.author == client.get_user(612522818294251522):
      embedVar = discord.Embed(
        title=f"Looking For Group Roles",
        description=
        "These roles are useful for finding people to play games with\nFor Example you can ping <@&1010118636305920041> and it would ping everyone that plays\nvalorant so you don't have to ping @everyone\n\nEach button below is a toggle for the game, if you don't want a game anymore, simply click that games button and it will be removed",
        colour=0x2f3136)
      embedVar.set_footer(text="Lunar Lounge")
      embedVar.set_author(name="Lunar Lounge・Self Roles 🪂")
      await msg.channel.send(embed=embedVar, view=lfgbuttons)


class lfgbuttons(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(label="Valorant")
  async def valorant(self, interaction: discord.Interaction,
                     Button: discord.ui.Button):
    await interaction.response.send_message("Test")


#------------ Global Slash Commands ------------


#First Form
class form_1(ui.Modal, title="LunarCraft Store Submission"):

  async def modal_1(interaction: discord.Interaction):
    name_of_store = ui.TextInput(label="Whats the name of your store?",
                                 placeholder="The name of my store is...",
                                 style=discord.TextStyle.short,
                                 required=True)
    store_sells = ui.TextInput(label="What does your store sell?",
                               placeholder="My store sells...",
                               style=discord.TextStyle.long,
                               required=True)
    get_stuff = ui.TextInput(label="How are people going to get your items?",
                             placeholder="To get stuff from my store...",
                             style=discord.TextStyle.long,
                             required=True)


#Second Form
class form_2(ui.Modal, title="LunarCraft Store Submission"):

  async def modal_2(interaction: discord.Interaction):
    name_of_store = ui.TextInput(label="Whats the name of your store?",
                                 placeholder="The name of my store is...",
                                 style=discord.TextStyle.short,
                                 required=True)
    store_sells = ui.TextInput(label="What does your store sell?",
                               placeholder="My store sells...",
                               style=discord.TextStyle.long,
                               required=True)
    get_stuff = ui.TextInput(label="How are people going to get your items?",
                             placeholder="To get stuff from my store...",
                             style=discord.TextStyle.long,
                             required=True)


#Third Form
class form_3(ui.Modal, title="LunarCraft Store Submission"):

  async def modal_3(interaction: discord.Interaction):
    name_of_store = ui.TextInput(label="Whats the name of your store?",
                                 placeholder="The name of my store is...",
                                 style=discord.TextStyle.short,
                                 required=True)
    store_sells = ui.TextInput(label="What does your store sell?",
                               placeholder="My store sells...",
                               style=discord.TextStyle.long,
                               required=True)
    get_stuff = ui.TextInput(label="How are people going to get your items?",
                             placeholder="To get stuff from my store...",
                             style=discord.TextStyle.long,
                             required=True)


#Fourth Form
class form_4(ui.Modal, title="LunarCraft Store Submission"):

  async def modal_4(interaction: discord.Interaction):
    name_of_store = ui.TextInput(label="Whats the name of your store?",
                                 placeholder="The name of my store is...",
                                 style=discord.TextStyle.short,
                                 required=True)
    store_sells = ui.TextInput(label="What does your store sell?",
                               placeholder="My store sells...",
                               style=discord.TextStyle.long,
                               required=True)
    get_stuff = ui.TextInput(label="How are people going to get your items?",
                             placeholder="To get stuff from my store...",
                             style=discord.TextStyle.long,
                             required=True)


#Fifth Form
class form_5(ui.Modal, title="LunarCraft Store Submission"):

  async def modal_5(interaction: discord.Interaction):
    name_of_store = ui.TextInput(label="Whats the name of your store?",
                                 placeholder="The name of my store is...",
                                 style=discord.TextStyle.short,
                                 required=True)
    store_sells = ui.TextInput(label="What does your store sell?",
                               placeholder="My store sells...",
                               style=discord.TextStyle.long,
                               required=True)
    get_stuff = ui.TextInput(label="How are people going to get your items?",
                             placeholder="To get stuff from my store...",
                             style=discord.TextStyle.long,
                             required=True)


#Ping Command for Checking bot status
@tree.command(name="ping", description="Check if the bot is online")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message("🏓 Pong!")


#Make a Poll in Discord in 2 Seconds
@tree.command(name="poll", description="Make a Poll Easily")
@app_commands.checks.bot_has_permissions(view_channel=True)
@app_commands.choices(type=[
  Choice(name="Simple Yes/No Poll", value="poll1"),
  Choice(name="Customized Multiple Choice Poll", value="poll2"),
])
async def hello(interaction: discord.Interaction, type: str):
  if not interaction.user.guild_permissions.manage_guild:
    await interaction.response.send_message(
      "This command is only available to users with the Manage Server permission",
      ephemeral=True)
  else:
    if type == "poll1":
      await interaction.response.send_modal(simple_poll())
    if type == "poll2":
      await interaction.response.send_modal(poll())


#Advanced Poll Modal
class poll(ui.Modal, title="Poll Creator"):
  question = ui.TextInput(label="Question",
                          placeholder="Poll Question",
                          style=discord.TextStyle.short,
                          required=True)
  option_1 = ui.TextInput(label="Option 1",
                          placeholder="Option 1",
                          style=discord.TextStyle.short,
                          required=True)
  option_2 = ui.TextInput(label="Option 2",
                          placeholder="Option 2",
                          style=discord.TextStyle.short,
                          required=True)
  option_3 = ui.TextInput(label="Option 3",
                          placeholder="Option 3",
                          style=discord.TextStyle.short,
                          required=False)
  option_4 = ui.TextInput(label="Option 4",
                          placeholder="Option 4",
                          style=discord.TextStyle.short,
                          required=False)

  async def on_submit(self, interaction: discord.Interaction):
    question = str(self.question)
    if "?" in question:
      actual_question = question
    if not "?" in question:
      actual_question = question + "?"
    option_1 = str(self.option_1)
    option_2 = str(self.option_2)
    option_3 = str(self.option_3)
    option_4 = str(self.option_4)
    description = "1️⃣ " + option_1 + "" + "\n2️⃣ " + option_2 + ""
    actual_description = description
    if not option_3 == "":
      actual_description = description + "\n3️⃣ " + option_3
    if not option_4 == "":
      actual_description = actual_description + "\n4️⃣ " + option_4
    embedVar = discord.Embed(title=actual_question,
                             description=actual_description,
                             colour=0x2F3136)
    name = interaction.user.name + "#" + str(interaction.user.discriminator)
    embedVar.set_author(name=name, icon_url=str(interaction.user.avatar))
    await interaction.response.send_message("Your poll Was Created!",
                                            ephemeral=True)
    message = await interaction.channel.send(embed=embedVar)
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    if not option_3 == "":
      await message.add_reaction('3️⃣')
    if not option_4 == "":
      await message.add_reaction('4️⃣')


#Simple Poll Modal
class simple_poll(ui.Modal, title="Simple Poll"):
  question = ui.TextInput(label="Poll Question",
                          placeholder="Enter a Question",
                          style=discord.TextStyle.short,
                          required=True)

  async def on_submit(self, interaction: discord.Interaction):
    question = str(self.question)
    if not question == "":
      if "?" in question:
        actual_question = question
      if not "?" in question:
        actual_question = question + "?"
      embedVar = discord.Embed(title=actual_question, colour=0x2F3136)
      name = interaction.user.name + "#" + str(interaction.user.discriminator)
      embedVar.set_author(name=name, icon_url=str(interaction.user.avatar))
      await interaction.response.send_message("Your poll Was Created!",
                                              ephemeral=True)
      message = await interaction.channel.send(embed=embedVar)
      await message.add_reaction('👍')
      await message.add_reaction('👎')


#Math Command
@tree.command(name="equation", description="Make me do some Math!")
@app_commands.choices(operation=[
  Choice(name="x", value="multiply"),
  Choice(name="-", value="subtract"),
  Choice(name="+", value="plus"),
  Choice(name="÷", value="divide"),
])
async def hello(interaction: discord.Interaction, number_1: int,
                operation: str, number_2: int):
  if operation == "multiply":
    answer = number_1 * number_2
  elif operation == "subtract":
    answer = number_1 - number_2
  elif operation == "plus":
    answer = number_1 + number_2
  elif operation == "divide":
    answer = number_1 / number_2
  await interaction.response.send_message(str(answer))


#Cat Command
@tree.command(name="cat", description="Get a random picture of a cat")
async def hello(interaction: discord.Interaction):
  from generator import catimages
  catimage = random.choice(catimages)
  await interaction.response.send_message(catimage)


#Dog Command
@tree.command(name="dog", description="Get a random picture of a dog")
async def hello(interaction: discord.Interaction):
  from generator import dogimages
  dogimage = random.choice(dogimages)
  await interaction.response.send_message(dogimage)


#Bird Command
@tree.command(name="bird", description="Get a random picture of a bird")
async def hello(interaction: discord.Interaction):
  from generator import birdimages
  birdimage = random.choice(birdimages)
  await interaction.response.send_message(birdimage)


#Help command
@tree.command(name="help", description="Use /commands instead")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(
    "The help command has been replaced by ``/commands``", ephemeral=True)


#See the latest changelog on the bot
@tree.command(name="changelog", description="See the latest Panda.py updatyes")
async def hello(interaction: discord.Interaction):
  embedVar = discord.Embed(
    title="Recent Updates on the Panda.py Discord Bot",
    description=
    "```- Brand New /poll command with Simple Yes/No Polls and Extremely Customizeable Polls``````- Webhooks are having problems so we have temporarily replaced webhook in /embed with Thumbnails until we find a way to get webhooks working again``````- New /equations command that does math for you using Python, it has been made to be able to do calculations almost instantly```",
    colour=0x2F3136)
  embedVar.set_footer(text="pandabot.xyz",
                      icon_url="https://i.imgur.com/6RRyN30.png")
  embedVar.set_author(
    name="Atomic#0100",
    icon_url=
    "https://cdn.discordapp.com/avatars/612522818294251522/ec6b0ba95f471d2844fcc47d16f4ec02.png?size=1024"
  )
  await interaction.response.send_message(embed=embedVar)


#Goodnight Command
@tree.command(name="goodnight",
              description="For if nobody will say goodnight to you")
async def hello(interaction: discord.Interaction):
  channel = client.get_channel(998549944342413332)
  if not interaction.channel == channel:
    goodnight_messages = [
      "(╯°□°)╯︵ ┻━┻ Goodnight (╯°□°)╯︵ ┻━┻", "¯\_(ツ)_/¯ Goodnight ¯\_(ツ)_/¯",
      "┬─┬ノ( º _ ºノ) Goodnight ┬─┬ノ( º _ ºノ)"
    ]
    goodnight_response = random.choice(goodnight_messages)
    await interaction.response.send_message(goodnight_response)
  else:
    await interaction.response.send_message(
      "``Your message was forwarded to Lunar``")
    async with aiohttp.ClientSession() as session:
      user = interaction.user
      goodnight_messages = [
        f"(╯°□°)╯︵ ┻━┻ Goodnight <@{user.id}> (╯°□°)╯︵ ┻━┻",
        f"¯\_(ツ)_/¯ Goodnight <@{user.id}> ¯\_(ツ)_/¯",
        f"┬─┬ノ( º _ ºノ) Goodnight <@{user.id}> ┬─┬ノ( º _ ºノ)"
      ]
      goodnight_response = random.choice(goodnight_messages)
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      await webhook.send(goodnight_response)


#Review System for servers
@tree.command(name="review",
              description="Send a review in your current server")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(
    "Server Reviews are not ready for public use", ephemeral=True)


#Command to setup stuff on Panda.py
@tree.command(name="setup", description="Setup a Module on your server")
@app_commands.choices(module=[
  Choice(name="Server Review System", value="reviewsystem"),
  Choice(name="Join Messages", value="joinmessages"),
  Choice(name="Leave Messages", value="leavemessages")
])
async def hello(interaction: discord.Interaction, module: str):

  if interaction.user.guild_permissions.manage_guild:
    if module == "reviewsystem":
      await interaction.response.send_message(
        "The server review module is still in development and is not ready for public use",
        ephemeral=True)
    if module == "joinmessages":
      await interaction.response.send_message(
        "Join Messages Are Still in development and are not ready for public use",
        ephemeral=True)
    if module == "leavemessages":
      await interaction.response.send_message(
        "Leave Messages Are Still in development and are not ready for public use",
        ephemeral=True)
  else:
    await interaction.response.send_message(
      "This command is only available to users with the Manage Server permission",
      ephemeral=True)


#Modal for setting up join messages
class join_messages_modal(ui.Modal, title="Setup Join Messages"):
  embed_title = ui.TextInput(label="Embed Title",
                             placeholder="Enter a title",
                             style=discord.TextStyle.short,
                             required=False)
  embed_description = ui.TextInput(
    label="Embed Description",
    placeholder="Use {member} to mention the joining member",
    style=discord.TextStyle.long,
    required=False)
  embed_footer = ui.TextInput(label="Embed Footer",
                              placeholder="Enter a footer",
                              style=discord.TextStyle.short,
                              required=False)
  channel_id = ui.TextInput(label="Destination Channel ID",
                            placeholder="Enter a Channel ID",
                            style=discord.TextStyle.short,
                            required=True)

  async def on_submit(self, interaction: discord.Interaction):
    title = f"{interaction.guild_id}-embed_title"
    description = f"{interaction.guild_id}-embed_description"
    destination_channel = f"{interaction.guild_id}-channel_id"
    db.join_messages.insert_one({
      title: str(self.embed_title),
      description: str(self.embed_description),
      destination_channel: str(self.channel_id),
    })
    await interaction.response.send_message("Successfully Setup Join Messages")


#Command to flip a coin
@tree.command(name="flip", description="Flip a coin!")
async def hello(interaction: discord.Interaction):
  coin_flip = ["Heads", "Tails"]
  result = random.choice(coin_flip)
  await interaction.response.send_message(result)


#Roll a dice
@tree.command(name="roll", description="Roll a random dice")
async def media(interaction: discord.Interaction):
  number_list = ["1", "2", "3", "4", "5", "6"]
  number = random.choice(number_list) + "/6"
  await interaction.response.send_message(number)


#Gif Command for sending a random gif to chat
@tree.command(name="gif", description="Send a random gif to chat")
async def hello(interaction: discord.Interaction):
  from media import gif_list
  choice = random.choice(gif_list)
  await interaction.response.send_message(choice)
  print("/gif was just used")


#Information about the bot
@tree.command(name="about", description="Some information about me!")
async def hello(interaction: discord.Interaction):
  embedVar = discord.Embed(colour=0x2F3136)
  embedVar.add_field(
    name="About Me",
    value=
    "Panda is a multipurpose Discord bot focused on redesigning popular commands and adding essential features to your Discord Server, we use high performance hardware so that your Discord Server is never missing essential features",
    inline=False)
  embedVar.add_field(
    name="Website",
    value=
    "[Homepage](https://pandabot.xyz)・[Commands](https://pandabot.xyz/commands)・[Privacy](https://pandabot.xyz/privacy)",
    inline=True)
  embedVar.add_field(
    name="Bot Ping",
    value=
    f"``{round (client.latency * 1000)}ms`` to the closest Discord Websocket",
    inline=True)
  await interaction.response.send_message(embed=embedVar)
  print("/about was just used")


#Warning Command
@tree.command(name="warning", description="Send a warning to chat")
async def warning(interaction: discord.Interaction, message: str):
  embedVar = discord.Embed(colour=0x2F3136,
                           description=f"⚠ Warning: {message}")
  await interaction.response.send_message(embed=embedVar)
  print("/warning was just used")


#Help command/commands overview command
@tree.command(name="commands", description="Get help with the bot")
@app_commands.choices(type=[
  Choice(name="Fun Commands", value="funcommands"),
  Choice(name="All Commands", value="allcmds"),
  Choice(name="Utility Commands", value="utilitycommands"),
  Choice(name="Context Menu Apps", value="contextmenuapps"),
  Choice(name="Search For a Command", value="cmdsearch"),
])
async def warning(interaction: discord.Interaction, type: str):
  if type == "contextmenuapps":
    embedVar = discord.Embed(
      colour=0x2F3136,
      title="Context Menu Apps",
      description="These commands are used with context menus")
    embedVar.add_field(
      name="Avatar",
      value="Send the avatar of the message author to your current chat",
      inline=True)
    embedVar.add_field(
      name="Convert to Embed",
      value="Convert the included message to an embed with the message author",
      inline=True)
    embedVar.add_field(
      name="Echo",
      value="Send the contents of the message provided through Panda",
      inline=True)
    embedVar.add_field(
      name="Fetch Media",
      value=
      "We will search for keywords to find media that relates with the message that is provided in the context menu",
      inline=True)
    embedVar.set_footer(text="pandabot.xyz",
                        icon_url="https://i.imgur.com/6RRyN30.png")
    embedVar.add_field(
      name="Social Links",
      value=
      "[Website](https://pandabotwebsite.carrd.co/)・[Invite Panda](https://discord.com/api/oauth2/authorize?client_id=1059436505711517756&permissions=275750841446&scope=bot%20applications.commands)・[Vote on Top.gg](https://top.gg/bot/1059436505711517756/vote)",
      inline=False)
    await interaction.response.send_message(embed=embedVar)
  elif type == "allcmds":
    embedVar = discord.Embed(colour=0x2F3136,
                             title="All Commands",
                             description="All commands on Panda.py")
    embedVar.add_field(name="/warning",
                       value="Simply sends a warning to chat",
                       inline=True)
    embedVar.add_field(name="/ping",
                       value="Checks if the bot is up and functioning",
                       inline=True)
    embedVar.add_field(name="/about",
                       value="Some basic info about Panda.py",
                       inline=True)
    embedVar.add_field(name="/embed",
                       value="Bring up the embed builder in Discord",
                       inline=True)
    embedVar.add_field(name="/media",
                       value="Browse our media library",
                       inline=True)
    embedVar.add_field(name="/gif",
                       value="Send a completely random gif to chat",
                       inline=True)
    embedVar.add_field(name="/flip",
                       value="Flip a coin and get the result",
                       inline=True)
    embedVar.add_field(name="/roll",
                       value="Roll a 6 sided dice and get the result",
                       inline=True)
    embedVar.add_field(name="/embed",
                       value="Make an embed and send it to your chat!",
                       inline=True)
    embedVar.add_field(
      name="/goodnight",
      value="For if its 2am and nobody will say goodnight to you",
      inline=True)
    embedVar.add_field(name="/suggest",
                       value="Suggest a new feature for the bot",
                       inline=True)
    embedVar.add_field(name="/commands",
                       value="See placeholders for certain things",
                       inline=True)
    embedVar.add_field(name="/echo",
                       value="Echo a message in your current channel",
                       inline=True)
    embedVar.add_field(name="/bug",
                       value="Report a bug to the Developers",
                       inline=True)
    embedVar.add_field(name="/suggest",
                       value="Suggest a new feature for the bot",
                       inline=True)
    embedVar.add_field(
      name="/word",
      value="Generate a word with random letters from the alphabet",
      inline=True)
    embedVar.add_field(name="/disguise",
                       value="Disguise a link in a simple message",
                       inline=True)
    embedVar.add_field(name="/webhook",
                       value="Send a message through a webhook easily",
                       inline=True)
    embedVar.add_field(name="/dog",
                       value="Send a random dog picture to chat",
                       inline=True)
    embedVar.add_field(name="/cat",
                       value="Send a random cat picture to chat",
                       inline=True)
    embedVar.add_field(name="/bird",
                       value="Send a random bird picture to chat",
                       inline=True)
    embedVar.set_footer(text="pandabot.xyz",
                        icon_url="https://i.imgur.com/6RRyN30.png")
    embedVar.add_field(
      name="Social Links",
      value=
      "[Website](https://pandabotwebsite.carrd.co/)・[Invite Panda](https://discord.com/api/oauth2/authorize?client_id=1059436505711517756&permissions=275750841446&scope=bot%20applications.commands)・[Vote on Top.gg](https://top.gg/bot/1059436505711517756/vote)",
      inline=False)
    await interaction.response.send_message(embed=embedVar)
  elif type == "utilitycommands":
    embedVar = discord.Embed(
      colour=0x2F3136,
      title="Utility Commands",
      description="Commands used to supercharge your server")
    embedVar.add_field(name="/embed",
                       value="Instantly make an embed in your chat",
                       inline=True)
    embedVar.add_field(name="/about",
                       value="View info about the bot",
                       inline=True)
    embedVar.add_field(name="/commands",
                       value="Get help with commands on Panda-Bot",
                       inline=True)
    embedVar.add_field(name="/ping",
                       value="Get the bots ping to Discord",
                       inline=True)
    embedVar.add_field(name="/warning",
                       value="Send a warning to chat instantly",
                       inline=True)
    embedVar.add_field(name="/suggest",
                       value="Suggest a new feature for the bot",
                       inline=True)
    embedVar.add_field(name="/bug",
                       value="Report a bug to the Developers",
                       inline=True)
    embedVar.add_field(name="/echo",
                       value="Echo a message in your current channel",
                       inline=True)
    embedVar.set_footer(text="pandabot.xyz",
                        icon_url="https://i.imgur.com/6RRyN30.png")
    embedVar.add_field(
      name="Social Links",
      value=
      "[Website](https://pandabotwebsite.carrd.co/)・[Invite Panda](https://discord.com/api/oauth2/authorize?client_id=1059436505711517756&permissions=275750841446&scope=bot%20applications.commands)・[Vote on Top.gg](https://top.gg/bot/1059436505711517756/vote)",
      inline=False)
    await interaction.response.send_message(embed=embedVar)
  elif type == "funcommands":
    embedVar = discord.Embed(colour=0x2F3136,
                             title="Fun Commands",
                             description="Commands to use when your bored")
    embedVar.add_field(
      name="/flip",
      value="Flip a coin and get the result in your current chat",
      inline=True)
    embedVar.add_field(
      name="/gif",
      value="Send a completely random gif to your current chat",
      inline=True)
    embedVar.add_field(
      name="/media",
      value="Select media from our library to send to your chat",
      inline=True)
    embedVar.add_field(
      name="/goodnight",
      value="For if its 2am and nobody will say goodnight to you",
      inline=True)
    embedVar.add_field(
      name="/word",
      value="Try and make a word combination with random lettes",
      inline=True)
    embedVar.add_field(name="/cat",
                       value="Send a random cat picture to chat",
                       inline=True)
    embedVar.add_field(name="/dog",
                       value="Send a random dog picture to chat",
                       inline=True)
    embedVar.add_field(name="/bird",
                       value="Send a random bird picture to chat",
                       inline=True)
    embedVar.add_field(
      name="Social Links",
      value=
      "[Website](https://pandabotwebsite.carrd.co/)・[Invite Panda](https://discord.com/api/oauth2/authorize?client_id=1059436505711517756&permissions=275750841446&scope=bot%20applications.commands)・[Vote on Top.gg](https://top.gg/bot/1059436505711517756/vote)",
      inline=False)
    embedVar.set_footer(text="pandabot.xyz",
                        icon_url="https://i.imgur.com/6RRyN30.png")
    await interaction.response.send_message(embed=embedVar)
  elif type == "cmdsearch":
    await interaction.response.send_modal(commandsearch())
  print("/commands was just used")


#Modal For Searching our Command Database
class commandsearch(ui.Modal, title="Search For a Command"):
  command_name = ui.TextInput(label="Command Name",
                              placeholder="Enter the name of a Command",
                              style=discord.TextStyle.short,
                              required=True)

  async def on_submit(self, interaction: discord.Interaction):

    #Command information for /cat
    if str(self.command_name) == "cat" or str(self.command_name) == "Cat":
      embedVar = discord.Embed(title="The /cat Command", colour=0x2F3136)
      embedVar.add_field(
        name="What it does",
        value=
        "This command simply grabs a random picture of a Cat from our Pictures Database"
      )
      embedVar.add_field(
        name="Where are the images sourced from?",
        value=
        "All images on our bot that aren't made by us or given permission to us to use are sourced from https://pexels.com"
      )
      await interaction.response.send_message(embed=embedVar)

    #Command Information for /dog
    elif str(self.command_name) == "dog" or str(self.command_name) == "Dog":
      embedVar = discord.Embed(title="The /dog Command", colour=0x2F3136)
      embedVar.add_field(
        name="What it does",
        value=
        "This command simply grabs a random picture of a Dog from our Pictures Database"
      )
      embedVar.add_field(
        name="Where are the images sourced from?",
        value=
        "All images on our bot that aren't made by us or given permission to us to use are sourced from https://pexels.com"
      )
      await interaction.response.send_message(embed=embedVar)

    #Command Information for /bird
    elif str(self.command_name) == "bird" or str(self.command_name) == "Bird":
      embedVar = discord.Embed(title="The /bird Command", colour=0x2F3136)
      embedVar.add_field(
        name="What it does",
        value=
        "This command simply grabs a random picture of a Bird from our Pictures Database"
      )
      embedVar.add_field(
        name="Where are the images sourced from?",
        value=
        "All images on our bot that aren't made by us or given permission to us to use are sourced from https://pexels.com"
      )
      await interaction.response.send_message(embed=embedVar)

    #Command Information for /changelog
    elif str(self.command_name) == "changelog" or str(
        self.command_name) == "Changelog":
      embedVar = discord.Embed(title="The /changelog Command", colour=0x2F3136)
      embedVar.add_field(
        name="What it does",
        value="This command simply shows everything new on the Bot")
      embedVar.add_field(name="Who Develops the Bot?",
                         value="This bot is developed by ``Atomic#0100``")
      await interaction.response.send_message(embed=embedVar)

    #Command Information for /flip
    elif str(self.command_name) == "flip" or str(self.command_name) == "Flip":
      embedVar = discord.Embed(title="The /flip Command", colour=0x2F3136)
      embedVar.add_field(
        name="What it does",
        value="This command will flip a coin for you and give you the result")
      await interaction.response.send_message(embed=embedVar)

    #Command Information for /flip
    elif str(self.command_name) == "roll" or str(self.command_name) == "Roll":
      embedVar = discord.Embed(title="The /roll Command", colour=0x2F3136)
      embedVar.add_field(
        name="What it does",
        value="This command will roll a 6 sided dice and give you the result")
      await interaction.response.send_message(embed=embedVar)

    #Command not found response
    else:
      await interaction.response.send_message("Command not found",
                                              ephemeral=True)


#Media context menu Interaction
@tree.context_menu(name="Fetch Media")
async def media(interaction: discord.Interaction, message: discord.Message):
  if message.author != client.user:
    if "kys" in message.content.lower(
    ) or "kill yourself" in message.content.lower(
    ) or "kill ys" in message.content.lower(
    ) or "k yourself" in message.content.lower():
      await interaction.response.send_message(
        "https://tenor.com/view/dance-gif-23986564")
    if "nigger" in message.content.lower() or "nigga" in message.content.lower(
    ) or "nigerian slave" in message.content.lower(
    ) or "niger" in message.content.lower():
      await interaction.response.send_message(
        "https://tenor.com/view/ratiobozo-ratio-gif-23500921")
    if "cum" in message.content.lower():
      await interaction.response.send_message(
        "https://tenor.com/view/cumlover-sex-cum-deez-nuts-gif-19912597")
    else:
      await interaction.response.send_message(
        "No matching media found in the selected message", ephemeral=True)
      print("Fetch media was just used")
  else:
    await interaction.response.send_message("You can't use this app on me",
                                            ephemeral=True)


#Get a users avatar from one of their messages
@tree.context_menu(name="Avatar")
async def media(interaction: discord.Interaction, message: discord.Message):
  if message.author != client.user:
    user = message.author
    pfp = user.avatar
    username = user.name + "#" + f"{user.discriminator}"
    embedVar = discord.Embed(title=username, colour=0x4a4a4a)
    embedVar.set_image(url=str(pfp))
    await interaction.response.send_message(embed=embedVar)
    print("User Avatar was just used")
  else:
    await interaction.response.send_message("You can't use this app on me",
                                            ephemeral=True)


#Turn original text into an embed
@tree.context_menu(name="Convert to Embed")
async def media(interaction: discord.Interaction, message: discord.Message):
  if message.author != client.user:
    if "فرصفرصفر" in message.content or "احدصفرصفرصفرا" in message.content:
      await interaction.response.send_message(
        "This message is blocked by our content filter", ephemeral=True)
    else:
      user = message.author
      username = user.name + "#" + f"{user.discriminator}"
      embedVar = discord.Embed(title=username,
                               colour=0x4a4a4a,
                               description=f"{message.content}")
      await interaction.response.send_message(embed=embedVar)
      print("Convert to embed was just used")
  else:
    await interaction.response.send_message("You can't use this app on me",
                                            ephemeral=True)


#Echo a message already sent in chat
@tree.context_menu(name="Echo")
async def echo(interaction: discord.Interaction, message: discord.Message):
  if message.author != client.user:
    if "@" in message.content:
      await interaction.response.send_message(
        "You can't echo messages pinging other people", ephemeral=True)
    else:
      if "احدصفرصفرصفرا" in message.content:
        await interaction.response.send_message(
          "This message is blocked by our content filter", ephemeral=True)
      else:
        await interaction.response.send_message(message.content)
        print("Echo a message was just used")
  else:
    await interaction.response.send_message("I can't echo a message I sent",
                                            ephemeral=True)


#Media Slash Command
@tree.command(name="media", description="Find some media to send to chat")
@app_commands.choices(option=[
  Choice(name="BBC news but there is no news", value="bbcnewsbutnonews"),
  Choice(name="Never gonna give you up", value="rickroll"),
  Choice(name="Set Your Balls ABLAZE NOW", value="ballsablaze"),
  Choice(name="Very useful makeup tutorial", value="usefulmakeuptutorial"),
  Choice(name="We got the Uno Reverse", value="unoreverse"),
  Choice(name="Discord Moderators Be Like", value="discordmods"),
  Choice(name="Cum Goes Everywhere", value="cumgoeseverywhere"),
  Choice(name="I give u curry u give social security", value="indianscammers"),
  Choice(name="This Chat vibing", value="catvibing")
])
async def media(interaction: discord.Interaction, option: str):
  if option == "bbcnewsbutnonews":
    await interaction.response.send_message(
      "https://tenor.com/view/bbc-news-no-news-nothing-bbc-no-update-gif-25341446"
    )
  if option == "rickroll":
    rickroll_list = [
      "https://tenor.com/view/hugs-rickroll-gif-24588121",
      "https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713",
      "https://tenor.com/view/rickroll-gif-20435173"
    ]
    rickroll = random.choice(rickroll_list)
    await interaction.response.send_message(rickroll)
  if option == "ballsablaze":
    ballsablazelist = [
      "https://tenor.com/view/flame-hashira-gif-25030349",
      "https://tenor.com/view/set-your-balls-ablaze-rengoku-set-your-heart-ablaze-tanjiro-fire-gif-24716550",
      "https://tenor.com/view/rengoku-kyojuro-kyojuru-rengoku-set-your-heart-ablaze-set-your-balls-ablaze-rengoku-gif-25271829"
    ]
    ballsablaze = random.choice(ballsablazelist)
    await interaction.response.send_message(ballsablaze)
  if option == "usefulmakeuptutorial":
    await interaction.response.send_message(
      "https://tenor.com/view/makeup-failure-ugly-fat-girl-fatty-gif-20492889")
  if option == "unoreverse":
    unoreverselist = [
      "https://tenor.com/view/uno-reverse-uno-reverse-card-uno-no-u-gif-23863535",
      "https://tenor.com/view/reverse-card-uno-uno-cards-gif-13032597",
      "https://tenor.com/view/uno-card-reverse-gif-15490757"
    ]
    unoreverse = random.choice(unoreverselist)
    await interaction.response.send_message(unoreverse)
  if option == "discordmods":
    discordmodslist = [
      "https://tenor.com/view/discord-moderator-mods-discord-gif-19245121",
      "https://tenor.com/view/discord-mod-discord-mods-mute-ban-kick-gif-18546458",
      "https://tenor.com/view/discord-mod-discord-when-the-pov-kitten-gif-20824761"
    ]
    discordmoddresponse = random.choice(discordmodslist)
    await interaction.response.send_message(discordmoddresponse)
  if option == "cumgoeseverywhere":
    cumgoeseverywherelist = [
      "https://tenor.com/view/cum-gif-20774970",
      "https://tenor.com/view/cum-penis-cum-i-creamed-cumming-xd-gif-20404521"
    ]
    cumgoeseverywhere = random.choice(cumgoeseverywherelist)
    await interaction.response.send_message(cumgoeseverywhere)
  if option == "indianscammers":
    await interaction.response.send_message(
      "https://tenor.com/view/indian-call-center-gif-23348690")
  if option == "catvibing":
    await interaction.response.send_message(
      "https://tenor.com/view/happy-pleased-gif-24458226")
  print("/media was just used in chat")


#Random Word Generator Command
@tree.command(
  name="word",
  description=
  "Generate a random word, this just puts a bunch of random letters together")
@app_commands.choices(option=[
  Choice(name="3 Letter Word", value="3letter"),
  Choice(name="4 Letter Word", value="4letter"),
  Choice(name="5 Letter Word", value="5letter"),
  Choice(name="6 Letter Word", value="6letter"),
  Choice(name="7 Letter Word", value="7letter")
])
async def word(interaction: discord.Interaction, option: str):
  from generator import letters
  if option == "5letter":
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    letter4 = random.choice(letters)
    letter5 = random.choice(letters)
    await interaction.response.send_message(letter1 + letter2 + letter3 +
                                            letter4 + letter5)
  if option == "4letter":
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    letter4 = random.choice(letters)
    await interaction.response.send_message(letter1 + letter2 + letter3 +
                                            letter4)
  if option == "6letter":
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    letter4 = random.choice(letters)
    letter5 = random.choice(letters)
    letter6 = random.choice(letters)
    await interaction.response.send_message(letter1 + letter2 + letter3 +
                                            letter4 + letter5 + letter6)
  if option == "3letter":
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    await interaction.response.send_message(letter1 + letter2 + letter3)
  if option == "7letter":
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    letter4 = random.choice(letters)
    letter5 = random.choice(letters)
    letter6 = random.choice(letters)
    letter7 = random.choice(letters)
    await interaction.response.send_message(letter1 + letter2 + letter3 +
                                            letter4 + letter5 + letter6 +
                                            letter7)


#Modal For Making a basic embed
class embed_builder(ui.Modal, title="Embed Builder"):
  embed_title = ui.TextInput(label="Embed Title",
                             placeholder="Enter a title",
                             style=discord.TextStyle.short,
                             required=False)
  embed_description = ui.TextInput(label="Embed Description",
                                   placeholder="Enter a description",
                                   style=discord.TextStyle.long,
                                   required=False)
  embed_footer = ui.TextInput(label="Embed Footer",
                              placeholder="Enter a footer",
                              style=discord.TextStyle.short,
                              required=False)
  embed_image = ui.TextInput(label="Embed Image",
                             placeholder="Enter an image link",
                             style=discord.TextStyle.short,
                             required=False)
  embed_thumbnail = ui.TextInput(label="Embed Thumbnail",
                                 placeholder="Enter an image link",
                                 style=discord.TextStyle.short,
                                 required=False)

  async def on_submit(self, interaction: discord.Interaction):
    embedVar = discord.Embed(title=self.embed_title,
                             description=self.embed_description,
                             colour=0x2F3136)
    actual_thumbnail = str(self.embed_thumbnail)
    embedVar.set_thumbnail(url=actual_thumbnail)
    actual_image = str(self.embed_image)
    embedVar.set_image(url=actual_image)
    footer_text = str(self.embed_footer)
    embedVar.set_footer(text=f"{footer_text}")
    channel = client.get_channel(interaction.channel_id)
    if str(self.embed_title) == "" and str(
        self.embed_description) == "" and str(self.embed_footer) == "" and str(
          self.embed_image) == "" and str(self.embed_webhook_link) == "":
      await interaction.response.send_message("I can't send an empty embed",
                                              ephemeral=True)
    else:
      await channel.send(embed=embedVar)
      await interaction.response.send_message("Embed Sent", ephemeral=True)
      print("A message was sent with /embed")


#Embed Slash Command
@tree.command(name="embed", description="Open the Embed Builder in Discord")
@app_commands.choices(fields=[
  Choice(name="No Extra Fields", value="0"),
  Choice(name="1 Extra Field", value="1"),
  Choice(name="2 Extra Fields", value="2"),
  Choice(name="3 Extra Fields", value="3"),
])
@app_commands.checks.bot_has_permissions(send_messages=True)
async def media(interaction: discord.Interaction, fields: str):
  if not interaction.user.guild_permissions.manage_guild:
    await interaction.response.send_message(
      "You require the Manage Server permission to send/make embeds",
      ephemeral=True)
  else:
    if fields == "0":
      await interaction.response.send_modal(embed_builder())
      print("/embed was used")
    else:
      await interaction.response.send_message(
        "Extra fields are currently not supported yet", ephemeral=True)


#Command for reporting bugs to the developers
@tree.command(name="bug", description="Report a bug to the developers")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_modal(bug_report_modal())


#Report a Bug Modal
class bug_report_modal(ui.Modal, title="Report a Bug"):
  report_bug_found = ui.TextInput(label="Whats the bug you've found?",
                                  placeholder="Enter the bug you found",
                                  style=discord.TextStyle.long,
                                  required=True)
  report_bug_extra_info = ui.TextInput(
    label="Extra Information",
    placeholder="Input any extra information (Optional)",
    style=discord.TextStyle.short,
    required=False)

  async def on_submit(self, interaction: discord.Interaction):
    if "فرصفرصفر" in str(
        self.report_bug_found).lower() or "احدصفرصفرصفرا" in str(
          self.report_bug_found).lower() or "nigger" in str(
            self.report_bug_found).lower() or "nigga" in str(
              self.report_bug_found).lower() or "cunt" in str(
                self.report_bug_found).lower() or "fuck" in str(
                  self.report_bug_found).lower() or "فرصفرصفر" in str(
                    self.report_bug_found).lower() or "احدصفرصفرصفرا" in str(
                      self.report_bug_found).lower() or "nigger" in str(
                        self.report_bug_extra_info).lower() or "nigga" in str(
                          self.report_bug_found).lower() or "cunt" in str(
                            self.report_bug_found).lower() or "fuck" in str(
                              self.report_bug_extra_info).lower():
      await interaction.response.send_message(
        "This report was blocked by our content filter", ephemeral=True)
    else:
      await interaction.response.send_message(
        "Message was sent to the Developers! Thanks for your report",
        ephemeral=True)
      user = interaction.user
      message = str(self.report_bug_found)
      username = user.name + "#" + f"{user.discriminator}"
      embedVar = discord.Embed(title=username, colour=0x2F3136)
      embedVar.add_field(name="Bug Found",
                         value=self.report_bug_found,
                         inline=False)
      if not str(self.report_bug_extra_info) == "":
        embedVar.add_field(name="Extra Bug Info",
                           value=self.report_bug_extra_info,
                           inline=False)
      embedVar.set_footer(text="Panda.py Bug Report")
      channel = client.get_channel(1066793863899000925)
      await channel.send(embed=embedVar)
      print("/bug was just used")


#Suggest a New Feature
@tree.command(name="suggest", description="Suggest a new feature to Panda")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_modal(feature_suggest_modal())


#Suggest a feature modal
class feature_suggest_modal(ui.Modal, title="Suggest a Feature"):
  suggest_suggestion = ui.TextInput(label="What feature should we add?",
                                    placeholder="Tell us what we should add",
                                    style=discord.TextStyle.long,
                                    required=True)

  async def on_submit(self, interaction: discord.Interaction):
    if "فرصفرصفر" in str(
        self.suggest_suggestion).lower() or "احدصفرصفرصفرا" in str(
          self.suggest_suggestion).lower() or "nigger" in str(
            self.suggest_suggestion).lower() or "nigga" in str(
              self.suggest_suggestion).lower() or "cunt" in str(
                self.suggest_suggestion).lower() or "fuck" in str(
                  self.suggest_suggestion).lower() or "فرصفرصفر" in str(
                    self.suggest_suggestion).lower() or "احدصفرصفرصفرا" in str(
                      self.suggest_suggestion).lower():
      await interaction.response.send_message(
        "This report was blocked by our content filter", ephemeral=True)
    else:
      await interaction.response.send_message(
        "Message was sent to the Developers! Thanks for helping us develop the bot!",
        ephemeral=True)
      user = interaction.user
      username = user.name + "#" + f"{user.discriminator}"
      embedVar = discord.Embed(title=username,
                               description=str(self.suggest_suggestion),
                               colour=0x2F3136)
      embedVar.set_footer(text="Panda.py Feature Suggestion")
      channel = client.get_channel(1066793851366428795)
      await channel.send(embed=embedVar)
      print("/suggest was just used")


#Echo Command for bot admins
@tree.command(name="echo", description="Send a message as Panda.py")
@app_commands.checks.bot_has_permissions(send_messages=True)
async def media(interaction: discord.Interaction):
  if interaction.user.guild_permissions.manage_guild:
    await interaction.response.send_modal(echo_command())
  else:
    await interaction.response.send_message(
      "This command is limited to users with the Manage Server permission",
      ephemeral=True)


#Modal for the echo command
class echo_command(ui.Modal, title="Echo"):
  echo_message = ui.TextInput(label="Message Content",
                              placeholder="Enter a message...",
                              style=discord.TextStyle.short,
                              required=True)

  async def on_submit(self, interaction: discord.Interaction):
    channel = client.get_channel(interaction.channel_id)
    await channel.send(self.echo_message)
    await interaction.response.send_message("Message Sent", ephemeral=True)


@tree.command(name="disguise", description="Disguise a message")
@app_commands.checks.bot_has_permissions(send_messages=True)
async def media(interaction: discord.Interaction):
  await interaction.response.send_modal(disguise_modal())


#Modal to disguise a message
class disguise_modal(ui.Modal, title="Disguise Content"):
  hidden_message = ui.TextInput(label="Cover Message",
                                placeholder="Enter some cover text",
                                style=discord.TextStyle.long,
                                required=True)
  actual_message = ui.TextInput(label="Embeded Link",
                                placeholder="Enter a Link",
                                style=discord.TextStyle.long,
                                required=True)

  async def on_submit(self, interaction: discord.Interaction):
    channel = client.get_channel(interaction.channel_id)
    message_to_send = str(
      self.hidden_message
    ) + "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ " + str(
      self.actual_message)
    await interaction.response.send_message(message_to_send)


#Webook Slash Command
@tree.command(name="webhook", description="Send a message through a webhook")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_modal(webhook_form())


#Webhook Modal
class webhook_form(ui.Modal, title="Webhook Messages"):
  message_content = ui.TextInput(label="Message Content",
                                 placeholder="Enter a message...",
                                 style=discord.TextStyle.long,
                                 required=True)
  webhook_link = ui.TextInput(
    label="Webhook Link",
    placeholder="https://discord.com/api/webhooks/example",
    style=discord.TextStyle.short,
    required=True)

  async def on_submit(self, interaction: discord.Interaction):
    async with aiohttp.ClientSession() as session:
      actual_webhook_link = str(self.webhook_link)
      webhook = Webhook.from_url(actual_webhook_link, session=session)
      await interaction.response.send_message("Message Sent", ephemeral=True)
      await webhook.send(self.message_content)


#Vote Command
@tree.command(name="vote", description="Vote for us on Top.gg!")
async def warning(interaction: discord.Interaction):
  await interaction.response.send_message(
    "Vote for us at https://top.gg/bot/1059436505711517756/vote")
  print("/vote was just used")


#Get Stats on the Bot
@tree.command(name="stats", description="Get stats about Panda.py")
@app_commands.checks.bot_has_permissions(send_messages=True)
async def media(interaction: discord.Interaction):
  embedVar = discord.Embed(
    title="Panda.py Stats",
    description=f"I am currently in {len(client.guilds)} servers",
    colour=0x4a4a4a)
  await interaction.response.send_message(embed=embedVar)


async def on_app_command_error(interaction, error):
  if isinstance(error, app_commands.BotMissingPermissions):
    await interaction.response.send_message(error, ephemeral=True)
  else:
    raise error


#------------ Lunar Lounge Slash Commands ------------


#Apply for something
@tree.command(name="lunar-form",
              description="Fill out a form",
              guild=discord.Object(id=998548528160837653))
@app_commands.choices(option=[
  Choice(name="LunarCraft Store Submission", value="1"),
  Choice(name="Lunar Hosting Signup", value="2"),
])
async def form(interaction: discord.Interaction, option: str):
  if option == "1":
    await interaction.response.send_modal(lunarcraft_store_form())
  if option == "2":
    await interaction.response.send_modal(lunarnode_hosting_form())


#LunarCraft Store Submission Form Modal
class lunarcraft_store_form(ui.Modal, title="LunarCraft Store Submission"):
  name_of_store = ui.TextInput(label="Whats the name of your store?",
                               placeholder="The name of my store is...",
                               style=discord.TextStyle.short,
                               required=True)
  store_sells = ui.TextInput(label="What does your store sell?",
                             placeholder="My store sells...",
                             style=discord.TextStyle.long,
                             required=True)
  get_stuff = ui.TextInput(label="How are people going to get your items?",
                           placeholder="To get stuff from my store...",
                           style=discord.TextStyle.long,
                           required=True)

  async def on_submit(self, interaction: discord.Interaction):
    embedVar = discord.Embed(
      title="LunarCraft Store Sumissions",
      colour=0x2F3136,
      description=f"Sumbitted by <@{interaction.user.id}>")
    embedVar.add_field(name="Store Name",
                       value=self.name_of_store,
                       inline=False)
    embedVar.add_field(name="What does the store sell",
                       value=self.store_sells,
                       inline=False)
    embedVar.add_field(name="How will users get stuff from your store",
                       value=self.get_stuff,
                       inline=False)
    channel = client.get_channel(1062439927066927114)
    await channel.send(embed=embedVar)
    await interaction.response.send_message("Submission Sent", ephemeral=True)


#Lunar Hosting Signup
class lunarnode_hosting_form(ui.Modal, title="Lunar Hosting Signup"):
  hosting_email = ui.TextInput(
    label="Whats your email?",
    placeholder="Use an email that you can log into",
    style=discord.TextStyle.short,
    required=True)
  hosting_password = ui.TextInput(label="Create a password",
                                  placeholder="Make a unique password",
                                  style=discord.TextStyle.short,
                                  required=True)
  hosting_username = ui.TextInput(label="Create a usernmae",
                                  placeholder="This wil be used to login",
                                  style=discord.TextStyle.short,
                                  required=True)
  hosting_mcuser = ui.TextInput(
    label="Minecraft Username",
    placeholder="This username will be operator by default",
    style=discord.TextStyle.short,
    required=True)

  async def on_submit(self, interaction: discord.Interaction):
    await interaction.response.send_message("Application Sumbitted!",
                                            ephemeral=True)
    embedVar = discord.Embed(
      title="Lunar Hosting Signup",
      colour=0x2F3136,
      description=f"Sumbitted by <@{interaction.user.id}>")
    embedVar.add_field(name="Email", value=self.hosting_email, inline=False)
    embedVar.add_field(name="Password",
                       value=self.hosting_password,
                       inline=False)
    embedVar.add_field(name="Username",
                       value=self.hosting_username,
                       inline=False)
    embedVar.add_field(name="Minecraft User",
                       value=self.hosting_mcuser,
                       inline=False)
    channel = client.get_channel(1062439927066927114)
    await channel.send(embed=embedVar)
    await interaction.response.send_message("Submission Sent", ephemeral=True)


#Tickets Slash Command
@tree.command(name="tickets",
              description="How to use tickets here in the Lunar Lounge",
              guild=discord.Object(id=998548528160837653))
async def tickets(interaction: discord.Interaction):
  await interaction.response.send_message(
    "Use ``-ticket open (reason-here)``to open a ticket in your current channel"
  )


#Shortcuts Slash Command
@tree.command(name="shortcuts",
              description="Some shortcuts in the Lunar Lounge",
              guild=discord.Object(id=998548528160837653))
async def hello(interaction: discord.Interaction):
  channel = client.get_channel(998549944342413332)
  if not interaction.channel == channel:
    if interaction.guild.id == 1054681613138673674 or interaction.guild.id == 998548528160837653:
      embedVar = discord.Embed(
        title="Shortcuts",
        colour=0x4a4a4a,
        description=
        "[Website](https://lunarinc.xyz)・[Rules](https://discord.com/channels/998548528160837653/998549963720097912)・[LFG Roles](https://discord.com/channels/998548528160837653/1022056077195477032/1028639595014918185)・[Theatre](https://discord.com/channels/998548528160837653/1053274348997328926)"
      )
      embedVar.set_footer(text="Lunar Lounge")
      await interaction.response.send_message(embed=embedVar)
  else:
    await interaction.response.send_message(
      "``Your message was forwarded to Lunar``")
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      embedVar = discord.Embed(
        title="Shortcuts",
        colour=0x2F3136,
        description=
        "[Website](https://lunarinc.xyz)・[Rules](https://discord.com/channels/998548528160837653/998549963720097912)・[LFG Roles](https://discord.com/channels/998548528160837653/1022056077195477032/1028639595014918185)・[Theatre](https://discord.com/channels/998548528160837653/1053274348997328926)"
      )
      embedVar.set_footer(text="Lunar Lounge")
      await webhook.send(embed=embedVar)


#RoleCMDs Slash Command
@tree.command(
  name="rolecmds",
  description="Commands that you can send in chat to get or remove roles",
  guild=discord.Object(id=998548528160837653))
async def rolecmds(interaction: discord.Interaction):
  channel = client.get_channel(998549944342413332)
  if not interaction.channel == channel:
    if interaction.guild.id == 1054681613138673674 or interaction.guild.id == 998548528160837653:
      embedVar = discord.Embed(
        title="Role Commands",
        colour=0x2F3136,
        description=
        "``-role lfg valorant``\n``-role lfg roblox``\n``-role lfg minecraft``\n``-role lfg overwatch``\n``-role lfg mw2``\n``-role lfg warzone``\n``-role lfg fortnite``\n``-role lfg rocket league``"
      )
      embedVar.set_footer(text="Lunar Lounge")
      await interaction.response.send_message(embed=embedVar)
  else:
    await interaction.response.send_message(
      "``Your message was forwarded to Lunar``")
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      embedVar = discord.Embed(
        title="Role Commands",
        colour=0x2F3136,
        description=
        "``-role lfg valorant``\n``-role lfg roblox``\n``-role lfg minecraft``\n``-role lfg overwatch``\n``-role lfg mw2``\n``-role lfg warzone``\n``-role lfg fortnite``\n``-role lfg rocket league``"
      )
      embedVar.set_footer(text="Lunar Lounge")
      await webhook.send(embed=embedVar)


#Rules Slash Command
@tree.command(name="rules",
              description="See the server rules",
              guild=discord.Object(id=998548528160837653))
async def hello(interaction: discord.Interaction):
  channel = client.get_channel(998549944342413332)
  if not interaction.channel == channel:
    if interaction.guild.id == 1054681613138673674 or interaction.guild.id == 998548528160837653:
      embedVar = discord.Embed(
        description=
        "```1. No Spamming, posting ip grabber links or self advertising``````2. No being racist (unless you're joking around)``````3. Don't post ip grabber links, personal information or anything else that could be used to deal harm to others```",
        colour=0x4a4a4a)
      await interaction.response.send_message(embed=embedVar)
  else:
    await interaction.response.send_message(
      "``Your message was forwarded to Lunar``")
    async with aiohttp.ClientSession() as session:
      webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/1060822769425731624/2RXglGi5wQOE_LV7HlYHbN2ftV67CNWKQd1j1StWm_f3nFR0OB4GDIalUm-Ttf6n2WV1',
        session=session)
      embedVar = discord.Embed(
        description=
        "```1. No Spamming, posting ip grabber links or self advertising``````2. No being racist (unless you're joking around)``````3. Don't post ip grabber links, personal information or anything else that could be used to deal harm to others```",
        colour=0x4a4a4a)
      embedVar.set_footer(text="Lunar Lounge")
      await webhook.send(embed=embedVar)


#Form to search Google
class searchform(ui.Modal, title="Search Google"):
  search_query = ui.TextInput(
    label="Query (What your searching)",
    placeholder="What you want to search google.com for",
    style=discord.TextStyle.short,
    required=True)

  async def on_submit(self, interaction: discord.Interaction):
    query = str(self.movie_query)
    pass


@tree.command(name="search", description="Search the web!")
async def search(interaction: discord.Interaction):
  await interaction.response.send_modal(searchform())


# ---------- CONSOLE - COMMANDHANDLER ------------
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.playing, name="bulblabs.org"))
  print(f"Connected to the Terminal (Logged in as {client.user})")
  try:
    synced = await tree.sync()
    synced2 = await tree.sync(guild=discord.Object(id=998548528160837653))
    print(f"Synced {len(synced + synced2)} command(s)")
  except Exception as e:
    print(e)
  while True:
    terminalInput = await client.loop.run_in_executor(None, input, "> ")
    terminalSplit = terminalInput.split(maxsplit=2)
    baseCmd = terminalSplit[0]
    if baseCmd == "echo":
      echoChannel = terminalSplit[1]
      if echoChannel == None:
        print(
          f'Error: {echoChannel} is an invalid channel ID or does not exist.')
      else:
        baseChannel = client.get_channel(int(echoChannel))
        await baseChannel.send(terminalSplit[2])
        print(
          f'Success: Sent "{terminalSplit[2]}" to channel with id "{echoChannel}"'
        )
    elif baseCmd == "help":
      print('    ~~~ Arguments prefix\'d in "$" are optional ~~~')
      print('    // Currently Implemented Commands //')
      print(
        '"echo" >> Sends a message to a channel\n  Syntax: "echo <channel-id> <message>"'
      )
      print('"help" >> Displays all commands in the bot\n  Syntax: "help"')
      print('    // To be Implemented //')
      print('"ping" >> Pings the Bot\n  Syntax: "ping"')
      print('"ban" >> Bans the Member\n  Syntax: "ban <user-id> <$reason>"')
      print('"kick" >> Kicks the Member\n  Syntax: "kick <user-id> <$reason>"')
      print(
        '"timeout" >> Timeouts the Member\n  Syntax: "timeout <user-id> <duration> <$reason>"\n  Aliases: "mute"'
      )
    elif baseCmd == "ping":
      print(f"{round (client.latency * 1000)}ms Ping to Discord")
    else:
      print('Error: Invalid Command, type "help" for help.')


# REGISTER

# API work in progress
#class api:
#class alerts:

#------------ Run The Bot ------------
try:
  web_server()
  client.run(TOKEN)
except:
  os.system("kill 1")
