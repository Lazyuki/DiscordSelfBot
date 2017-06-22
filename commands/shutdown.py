import discord
import globalVariables as gv

bot = gv.bot
me = gv.me

aliases = ['shutdown', 'sd', 'kill']

usage = 'turn off the bot'

async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    await me.edit_message(message, 'bye bot')
    print('shutting down...')
    await me.logout()
    await bot.logout()
