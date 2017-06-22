import discord
import globalVariables as gv

bot = gv.bot
me = gv.me
myID = gv.myID

aliases = ['tag', 'give', 'assign']

usage = 'Assigns the role. `/tag <role name> [ <; name> or  @mention ]`'\
        ' That ";" is important if you want to type in plain names. '\
        'IF no mentions or names, it picks the last person who sent a message.'

async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    li = content.split(';')
    r = None
    roles = message.server.roles
    for role in roles:
        if role.name.lower().startswith(li[0]):
            r = role
            break
    else:
        await me.edit_message(message, 'role not found: {}'.format(li[0]))
        return
    mem = None
    if message.mentions != []:
        mem = message.mentions[0]
    else:
        if len(li) == 2:
            mem = message.server.get_member_named(li[1].strip())
        else:
            async for log in bot.logs_from(message.channel, 10):
                if log.author.id != myID:
                    mem = log.author
                    break
    if mem is None:
        await me.edit_message(message, 'Nobody was found')
        return
    await me.add_roles(mem, r)
    await me.edit_message(message, 'hey {} you have the role '
                          '{} now'.format(mem.name, r.name))
