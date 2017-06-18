import discord
import asyncio
from discord import Client
from discord import http
import sys # for restart
import os  # for restart
import json

with open('config.json') as json_file:
    config = json.load(json_file)

my_token = config['my_token']
bot_token = config['bot_token']
prefix = config['prefix']
colors = config['colors']
spams = config['spams']

ALPHABETS = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳",
             "🇴","🇵","🇶","🇷","🇸","🇹","🇺","🇻","🇼","🇽","🇾","🇿"]; # For reactions

NUMS = ["zero", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine"]; # For Tiles

bot = Client()
me = Client()
me.login(my_token, bot=False)
me.http.token = my_token

@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))
    print('Selfbot for {}'.format(me.user.name))
    print('------------------')

@bot.event
async def on_message(message):
    if message.author.id != me.user.id:
        return
    if not message.content.startswith(prefix):
        return
    cmd = message.content.split()[0]
    if cmd == '/d':
        await delete(message)
    elif cmd == '/e':
        await embed(message)
    elif cmd == '/h':
        await help(message)
    elif cmd == '/r':
        await react(message)
    elif cmd == '/t':
        await tile(message)
    elif cmd == '/tag':
        await tag(message)
    elif cmd == '/no':
        await notif(message)
    elif cmd == '/gamerescape':
        await gamerescape(message)
    elif cmd == '/g':
        await getrole(message)
    elif cmd == '/restart':
        await restart(message)
    elif cmd == '/kill':
        await shutdown(message)


async def help(message):
    list = message.content.split()
    content = ''
    ch = message.channel
    await me.delete_message(message)
    if len(list) == 2:
        content = list[1]
    if content == '':
        await me.send_message(ch, 'Current commands are: d e g h r s t tag no \
                              restart kill. `/h <command>`for more detail')
    elif content == 'd':
        await me.send_message(ch, 'Delete: `/d [num of messages to delete.]` \
                              If no number was given, defaults to 1')
    elif content == 'e':
        await me.send_message(ch, 'Embed: `/e [title] ; [description] ; \
                              [color]` color defaults to green\nExample: \
                              `/e This is title; This is description; red`')
    elif content == 'g':
        await me.send_message(ch, 'Get role ID: `/g <first few letters of a \
                              role name (ignores case)>`')
    elif content == 'r':
        await me.send_message(ch, 'React: `/r <a word with no spaces> [id]` \
                              If no id was given it takes the first message \
                              in the channel, which is not by me.\n \
                              *Since it\'s a reaction, the word cannot contain\
                               2 same letters.*')
    elif content == 't':
        await me.send_message(ch, 'tiles: `/t <tile message>`')
    elif content == 'tag':
        await me.send_message(ch, 'tag: `/tag <first few letters of a \
                              role name (case insensitive)> [name or mention]` \
                              If no person was given, it looks up the last \
                              person before the /tag message. \
                              \nExample: `/tag mod @trustworthy-person`')
    elif content == 'no':
        await me.send_message(ch, 'notification: "Mark read" for the servers \
                              in the spam servers list. (configure in \
                              "config.ini")')
    elif content == 'restart':
        await me.send_message(ch, 'restart: restart the bot to apply any \
                              changes made since starting this bot the \
                              last time')
    elif content == 'kill':
        await me.send_message(ch, 'shutdown: shutdown the selfbot')

#embed
async def embed(message):
    s = message.content[3:]
    ch = message.channel
    await me.delete_message(message)

    list = [l.strip() for l in s.split(';')]
    if len(list) < 2:
        list.append('')
    if len(list) < 3:
        list.append('')
    else:
        if list[2] in colors:
            list[2] = discord.Color(colors.[list[2]])
        else:
            list[2] = discord.Color(colors.['green'])

    em = discord.Embed(title=list[0], description=list[1], color=list[2])
    await me.send_message(ch, embed=em)


#get role id
async def getrole(message):
    msg = message.content[3:]
    server = message.server
    ch = message.channel
    await me.delete_message(message)
    roles = server.roles
    for role in roles:
        if role.name.lower().startswith(msg.lower()):
            await me.send_message(ch, '{}: `{}`'.format(role.name, role.mention))
            return

#tiles
async def tile(message):
    msg = message.content[3:]
    ch = message.channel
    await me.delete_message(message)
    result = ''
    for c in msg:
        if c == ' ':
            result += ' ' * 5
        elif c == '!':
            result += ':bangbang:'
        elif c == '?':
            result += ':interrobang:'
        elif 48 <= ord(c) <= 57:
            result += ':{}:'.format(NUMS[int(c)])
        else:
            result += ':regional_indicator_{}:'.format(c)
    await me.send_message(ch, result)


#react
async def react(message):
    list = message.content.split()
    ch = message.channel
    await me.delete_message(message)
    msg = None
    if len(list) < 3:
        async for log in bot.logs_from(ch, 5):
            if log.author.id != me.user.id:
                msg = log
                break
    else:
        msg = me.get_message(ch, list[2])
    if msg == None:
        return
    for c in list[1]:
        await me.add_reaction(msg, ALPHABETS[ord(c) - 97])


#tag
async def tag(message):
    list = message.content.split()
    if len(list) < 2:
        return
    r = None
    roles = message.server.roles
    for role in roles:
        if role.name.lower().startswith(r):
            r = role
            break
    if r is None:
        return
    mem = None
    if message.mentions != []:
        mem = message.mentions[0]
    else:
        if len(list) == 3:
            mem = bot.get_member_named(list[2])
        else:
            async for log in bot.logs_from(ch, 5):
                if log.author.id != me.user.id:
                    mem = log.author
                    break
    if mem is None:
        return
    await me.add_roles(mem, r)
    await me.edit_message(message, 'hey {} you have the role \
                          {} now'.format(mem.name, r.name))


#delete
# only looks up 50 recent logs in the chat.
async def delete(message):
    ch = message.channel
    num = message.content[3:]
    num = 1 if num == '' else int(num)
    await me.delete_message(message)
    list = []
    async for log in bot.logs_from(ch, 50):
        if log.author.id == me.user.id:
            list.append(log)
    if list == []:
        return
    while num > 0 and list != []:
        await me.delete_message(list[0])
        list.pop(0)
        num -= 1


# this is for when you were going to type /shrug but somehow ended up typing 
# /gamerescape by mistake.
async def gamerescape(message):
    await me.edit_message(message, '┐(\'～`;)┌')

#restart
async def restart(message):
    await me.edit_message(message, 'bot will be back...')
    print('restarting...')
    print('-------------')
    await me.logout()
    await bot.logout()
    python = sys.executable
    os.execl(python, python, * sys.argv)

#exit
async def shutdown(message):
    await me.edit_message(message, 'bye bot')
    print('shutting down...')
    await me.logout()
    await bot.logout()

#notification delete
async def notif(message):
    await me.delete_message(message)
    for id in spams:
        r = http.Route('POST', '/guilds/{guild_id}/ack', guild_id=id)
        await me.http.request(r)

try:
    bot.run(bot_token, bot=False)
except:
    print('Error shutting down...')
finally:
    exit()
