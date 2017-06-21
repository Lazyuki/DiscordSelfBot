import discord

aliases = ['gamerescape']

usage = 'fixes `/gamerescape` into shrug'

async def cmd(message, content, bot, me, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    await me.edit_message(message, '┐(\'～`;)┌')
