import discord
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()

def add_guild(m_guild, m_server):
  db[m_guild] = m_server
  
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$addguild"):
    x = msg.split(" ", 3)[1:]
    m_guild = x[0]
    m_server = x[1]
    add_guild(m_guild, m_server)
    await message.channel.send("New guild added successfully.")

  if msg.startswith("$listguilds"):
    for key in db.keys():
      await message.channel.send(key + '           ' + db[key])

  if msg.startswith("$help"):
    await message.channel.send("$help - lists commands")
    await message.channel.send("$addguild <guildname> <mainchannel> - adds a guild and their main channel. Will overwrite previous data")
    await message.channel.send("$delguild <guildname> - deletes guild specified")
    await message.channel.send("$guild <guildname> - lists main server for guild specified")
    await message.channel.send("$listguilds - lists all guilds and main servers")
    
  if msg.startswith("$guild"):
    x = msg.split(" ", 3)[1:]
    m_guild = x[0]
    x = m_guild.lower()
    for key in db:
      y = key.lower()
      if x == y:
        await message.channel.send(db[key])
        break

  if msg.startswith("$delguild"):
    x = msg.split(" ", 3)[1:]
    m_guild = x[0]
    del db[m_guild]
    await message.channel.send("Guild deleted successfully.")

keep_alive()
client.run(os.getenv("TOKEN"))
