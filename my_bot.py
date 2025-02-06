import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
# def should_i_respond(user_message, user_name):
#   if "robot" in user_message:
#     return True
#   else:
#     return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
# def respond(user_message, user_name):
#   return f"""you said my name!!
#   {user_message.replace("robot", user_name)}"""


# REPEAT IN ALTERNATING CAPS
def should_i_respond_1(user_message, user_name):
  if "repeat after me" in user_message:
    return True
  else:
    return False

def respond_1(user_message, user_name):
  return alt_cap(user_message.replace("repeat after me: ", ""))

def alt_cap(text):
    new_string = ""
    for i in range(len(text)):
        character = text[i]
        if i%2 == 0:
            new_string = new_string + character.upper()
        else:
            new_string = new_string + character.lower()
    return new_string


# TELL ME A JOKE
def should_i_respond_2(user_message, user_name):
  if "tell me a joke" in user_message:
    return True
  else:
    return False

def respond_2(user_message, user_name):
  return "Why was the robot couple's anniversary in the fall?\nThey were autumn-mated!"


# RANDOM COLOR
def should_i_respond_3(user_message, user_name):
  if "color" in user_message:
    return True
  else:
    return False

def respond_3(user_message, user_name):
  color = random.choice(["black", "brown", "grey", "white", "red", "orange", "yellow", "green", "blue", "purple", "pink"])
  return color


# HI MY NAME IS
def should_i_respond_4(user_message, user_name):
  if "hi my name is" in user_message:
    return True
  else:
    return False

def respond_4(user_message, user_name):
  return f'Hi, {user_message.replace("hi my name is ", "")}, my name is robot!'


# POTATO
def should_i_respond_5(user_message, user_name):
  if "potato" in user_message:
    return True
  else:
    return False

def respond_5(user_message, user_name):
  return "I LOVE POTATOES! There are so many wants to eat them."