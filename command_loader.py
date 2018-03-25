import os
import re
import importlib
from sys import stdout
import time
import command.manager
modules = []
loadModulesList = [f for f in os.listdir('./commands') if re.match(r'[^_].*\.py', f)];
loadModulesStep = 100 / len(loadModulesList)
loadProgress = 0

#sys.path.insert(0, os.getcwd()+os.sep+'commands')

for i in loadModulesList:
    try:
        className = i[:-3]
        mod = importlib.import_module('commands.%s' % className)
        cmd = getattr(mod, className.title())()
        modules.append(cmd);
    except ImportError as err:
        print('Error:', err)
    loadProgress += loadModulesStep
    stdout.write("\r{}%".format(loadProgress))
    stdout.flush()
    time.sleep(0.1)
stdout.write('\n')

commandManager = command.manager.Manager(modules)


currentCommand = commandManager.parse_command("echo ura tfrhyf fdvh fdhfds")

com = currentCommand.get_current_command()
agvs = currentCommand.get_current_agvs()
for command in modules:
    if com == command.get_command():
        command.answer(agvs,commandManager)
