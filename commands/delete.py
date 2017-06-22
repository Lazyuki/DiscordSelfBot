import discord
import globalVariables as gv

bot = gv.bot
me = gv.me

aliases = ['d', 'del', 'delete']

usage = 'Delete: `/d [num of messages to delete.]` '\
        'If no number was given, defaults to 1'

#delete
# only looks up 50 recent logs in the chat.
async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    ch = message.channel
    num = 1 if content == '' else int(content)
    await me.delete_message(message)
    list = []
    async for log in bot.logs_from(ch, 50):
        if log.author.id == myID:
            list.append(log)
    if list == []:
        return
    while num > 0 and list != []:
        await me.delete_message(list[0])
        list.pop(0)
        num -= 1
