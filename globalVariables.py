import discord
import json
import os

_absolutePath = os.path.dirname(__file__)
_configPath = "config.json"
_path = os.path.join(_absolutePath, _configPath)

with open(_path) as json_file:
    config = json.load(json_file)

myToken = config['myToken']
botToken = config['botToken']
myID = config['myID']
prefix = config['prefix']
colors = config['colors']
spams = config['spams']

bot = discord.Client()
me = discord.Client()
cmds = {} # This gets filled in selfbot.py
