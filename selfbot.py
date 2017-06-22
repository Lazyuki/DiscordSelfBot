import discord
import asyncio
import globalVariables as gv
from datetime import datetime as dt
from cmds import import_functions as imp

cmds = imp() # import all the functions with their aliases

gv.cmds.update(cmds)
myToken = gv.myToken
botToken = gv.botToken
myID = gv.myID
prefix = gv.prefix

bot = gv.bot
me = gv.me
me.login(myToken, bot=False)
me.http.token = myToken

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
        await cmds[command](message, msg[len(command) + 2:])


bot.run(botToken, bot=False)
