import discord
import json

with open('config.json') as json_file:
    _config = json.load(json_file)

_colors = _config['colors']


aliases = ['e', 'embed']

usage = 'Embed: `/e [title] ; [description] ; [color]` color defaults'\
        'to green\nExample: `/e This is title; This is description; red`'

async def cmd(message, content, bot, me, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    ch = message.channel
    await me.delete_message(message)

    list = [l.strip() for l in content.split(';')]
    if len(list) < 3:
        list.append('')
        if len(list) < 3:
            list.append('') # if only title
    color_int = None
    if list[2] in _colors:
        color_int = int(_colors[list[2]], 16)
    else:
        color_int = int(_colors['green'], 16)
        
    em = discord.Embed(title=list[0], description=list[1],
                       color=color_int)
    await me.send_message(ch, embed=em)
