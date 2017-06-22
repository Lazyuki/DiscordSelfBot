import discord
import globalVariables as gv

bot = gv.bot
me = gv.me
myID = gv.myID

ALPHABETS = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳",
             "🇴","🇵","🇶","🇷","🇸","🇹","🇺","🇻","🇼","🇽","🇾","🇿"];

aliases = ['r', 'react']

usage = 'React: `/r <a word with no spaces> [id]` If no id was given '\
        'it takes the first message in the channel, which is not by me.\n '\
        '*Since it\'s a reaction, the word cannot contain 2 same letters.*'

#react
async def cmd(message, content, help=False):
    if help:
        await me.edit_message(message, usage)
        return
    list = content.split()
    ch = message.channel
    await me.delete_message(message)
    msg = None
    if len(list) < 2:
        async for log in bot.logs_from(ch, 5):
            if log.author.id != myID:
                msg = log
                break
    else:
        msg = me.get_message(ch, list[1])
    if msg == None:
        return
    for c in list[0]:
        await me.add_reaction(msg, ALPHABETS[ord(c) - 97])
