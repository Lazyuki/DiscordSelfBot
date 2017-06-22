import discord
import globalVariables as gv

bot = gv.bot
me = gv.me
colors = gv.colors

aliases = ['e', 'embed']

usage = 'Embed: `/e [title] ; [description] ; [color]` color defaults'\
        'to green\nExample: `/e This is title; This is description; red`'

async def cmd(message, content, help=False):
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
    colorInt = None
    if list[2] in colors:
        colorInt = int(colors[list[2]], 16)
    else:
        colorInt = int(colors['green'], 16)
        
    em = discord.Embed(title=list[0], description=list[1],
                       color=colorInt)
    await me.send_message(ch, embed=em)
