from glob import glob

def import_functions():
    commandMap = {}
    for file in glob('./commands/*.py'):
        f = file[11:-3]
        cmds = __import__('commands.' + f)
        aliases = eval('cmds.{}.aliases'.format(f))
        for alias in aliases:
            commandMap[alias] = eval('cmds.{}.cmd'.format(f))
    return commandMap
