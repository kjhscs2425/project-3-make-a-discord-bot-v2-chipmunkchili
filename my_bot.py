"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "repeat after me" in user_message:
    return True
  else:
    return False

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


def respond(user_message, user_name):
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