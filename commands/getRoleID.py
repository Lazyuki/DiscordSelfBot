import discord
import globalVariables as gv

bot = gv.bot
me = gv.me

aliases = ['g', 'getroleid']

usage = 'Get the role ID: `/g <role name (ignores case)>`'

async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    server = message.server
    ch = message.channel
    await me.delete_message(message)
    roles = server.roles
    for role in roles:
        if role.name.lower().startswith(content.lower()):
            await me.send_message(ch, '{}: `{}`'.format(role.name, role.mention))
            return
