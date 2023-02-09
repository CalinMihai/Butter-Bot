import os
import discord

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)
my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")


client.run(os.getenv('TOKEN'))