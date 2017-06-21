import discord
import json
from discord import http

with open('config.json') as json_file:
    config = json.load(json_file)

spams = config['spams']

aliases = ['no', 'mar', 'read', 'notif']

usage = '"Mark As Read" the annoying servers. Configure in config.json'

async def cmd(message, content, bot, me, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    await me.delete_message(message)
    for id in spams:
        r = http.Route('POST', '/guilds/{guild_id}/ack', guild_id=id)
        await me.http.request(r)
