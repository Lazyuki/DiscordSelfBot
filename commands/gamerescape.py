import discord
import globalVariables as gv

bot = gv.bot
me = gv.me

aliases = ['gamerescape']

usage = 'fixes `/gamerescape` into shrug'

async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    await me.edit_message(message, '┐(\'～`;)┌')
