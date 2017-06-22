import discord
import globalVariables as gv

bot = gv.bot
me = gv.me

NUMS = ["zero", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine"];

aliases = ['t', 'tile']

usage = 'tile: `/t <tile message>`'

async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    ch = message.channel
    await me.delete_message(message)
    result = ''
    for c in content:
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

