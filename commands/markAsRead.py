import discord
from discord import http
import globalVariables as gv

bot = gv.bot
me = gv.me
spams = gv.spams

aliases = ['no', 'mar', 'read', 'notif']

usage = '"Mark As Read" the annoying servers. Configure in config.json'

async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    await me.delete_message(message)
    for id in spams:
        r = http.Route('POST', '/guilds/{guild_id}/ack', guild_id=id)
        await me.http.request(r)
