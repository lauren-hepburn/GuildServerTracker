import discord
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()  

def string_length(string):
  count = 0
  for letter in string:
    count += 1
  return count
  
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  await client.change_presence(status=discord.Status.online, activity = discord.Game("$help"))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$addguild"):
    x = msg.split(" ", 3)[1:]
    m_guild = x[0]
    m_server = x[1]
    if string_length(m_server) == 4:
      db[m_guild] = m_server
      await message.channel.send("New guild added successfully.")
    else:
      await message.channel.send("Incorrect channel. Channel must be format of <Ser3> or <Med1>, etc.")

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
    x = m_guild.lower()
    for key in db:
      y = key.lower()
      if x == y:
        del db[key]
        await message.channel.send("Guild deleted successfully.")
        break

keep_alive()
client.run(os.getenv("TOKEN"))
