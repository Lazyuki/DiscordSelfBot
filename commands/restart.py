import discord
import os
import sys

aliases = ['rs', 'restart', 'reboot']

usage = 'restarts the bot'

async def cmd(message, content, bot, me, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    await me.edit_message(message, 'bot will be back...')
    print('Restarting...')
    print('-------------')
    await me.logout()
    await bot.logout()
    python = sys.executable
    os.execl(python, python, * sys.argv)
