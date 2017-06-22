import discord
import globalVariables as gv

bot = gv.bot
me = gv.me
cmds = gv.cmds

aliases = ['h', 'help', 'halp']

usage = 'Just `/h` to get help message savvy?'

async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    if content == '':
        await me.edit_message(message, '`/h <command>` for more info.\n'\
                              'Current commands are {}'.format(list(cmds.keys())))
        return
    if not content in cmds:
        await me.edit_message(message, 'Command not found: {}'.format(content))
        return
    await cmds[content](message, content, True)
