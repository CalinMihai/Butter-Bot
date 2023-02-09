import os
import discord
import requests
import json
import random


intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)
my_secret = os.environ['TOKEN']

sad_words = ["sad", "depressed", "depressing", "miserable"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You'll be fine!",
  "Will you quit winning?"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "\"" + json_data[0]['q'] + "\"" + " by " + json_data[0]['a']
  return (quote)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any (word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))