import discord
import asyncio
from discord import Client
import json
from datetime import datetime as dt
from cmds import import_functions as imp

cmds = imp() # import all the functions with their aliases

with open('config.json') as json_file:
    config = json.load(json_file)

my_token = config['my_token']
bot_token = config['bot_token']
myID = config['myID']
prefix = config['prefix']

bot = Client()
me = Client()
me.login(my_token, bot=False)
me.http.token = my_token

@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))
    name = None
    for server in bot.servers:
        if server.get_member(myID):
            name = server.get_member(myID).name
            break
    print('Selfbot for {}'.format(name))
    print('Now: {}'.format(dt.now().strftime('%a %b %d, %X')))
    print('------------------')

@bot.event
async def on_message(message):
    if message.author.id != myID:
        return
    if not message.content.startswith(prefix):
        return
    msg = message.content
    command = msg.split()[0][1:]
    if cmds[command]:
        await cmds[command](message, msg[len(command) + 2:], bot, me)


async def help(message, content, bot, me, help=False):
    if help:
        await me.edit_message(message, '/h h... really man?...')
        return
    if content == '':
        await me.edit_message(message, '`/h <command>` for more info. '\
                              'Current commands are {}'.format(list(cmds.keys())))
        return
    if not content in cmds:
        await me.edit_message(message, 'Command not found: {}'.format(content))
        return
    await cmds[content](message, content, bot, me, True)


# These assign the help function to be called on_message
cmds['h'] = help
cmds['help'] = help

try:
    bot.run(bot_token, bot=False)
except:
    print('Error shutting down...')
finally:
    exit()
