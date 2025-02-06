"""
Do NOT modify this file
(At least at first)

Instead, modify the functions in `my_bot.py`
"""

import os
import discord
import my_bot
from secret import *

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print("I'm in")
  print(client.user)

@client.event
async def on_message(message):
  if message.channel.name == "stella_bot":
    if message.author != client.user:
      user_name = message.author.display_name
      if my_bot.should_i_respond_1(message.content, user_name):
        response = my_bot.respond_1(message.content, user_name)
        await message.channel.send(response)
      elif my_bot.should_i_respond_2(message.content, user_name):
        response = my_bot.respond_2(message.content, user_name)
        await message.channel.send(response)
      elif my_bot.should_i_respond_3(message.content, user_name):
        response = my_bot.respond_3(message.content, user_name)
        await message.channel.send(response)
      elif my_bot.should_i_respond_4(message.content, user_name):
        response = my_bot.respond_4(message.content, user_name)
        await message.channel.send(response)
      elif my_bot.should_i_respond_5(message.content, user_name):
        response = my_bot.respond_5(message.content, user_name)
        await message.channel.send(response)
      # elif my_bot.should_i_respond_6(message.content, user_name):
      #   response = my_bot.respond_6(message.content, user_name)
      #   await message.channel.send(response)
      # elif my_bot.should_i_respond_7(message.content, user_name):
      #   response = my_bot.respond_7(message.content, user_name)
      #   await message.channel.send(response)
      # elif my_bot.should_i_respond_8(message.content, user_name):
      #   response = my_bot.respond_8(message.content, user_name)
      #   await message.channel.send(response)
      # elif my_bot.should_i_respond_9(message.content, user_name):
      #   response = my_bot.respond_9(message.content, user_name)
      #   await message.channel.send(response)
      # elif my_bot.should_i_respond_10(message.content, user_name):
      #   response = my_bot.respond_10(message.content, user_name)
      #   await message.channel.send(response)
      else:
        response = "What did you say?"
        await message.channel.send(response)

client.run(my_secret)