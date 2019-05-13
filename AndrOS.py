# -*- coding: utf-8 -*-
from colorama import init
from termcolor import colored
import time
import colorama
import start
import os
import re
import importlib
from sys import stdout
import splash
import codecs
import command.manager
import command.config
import command.color
import sys
import json

init()

devMode = ('DEV' in os.environ) if True else False

commandConfig = command.config.Config('config.json')

disk = commandConfig.get_disk()
lang = commandConfig.get_lang()
config = commandConfig.get_config()

version = commandConfig.get_version()


spl = splash.Splash()
if not devMode:
    spl.header_screen_writer()

# Load modules 
modules = []
loadModulesList = [f for f in os.listdir('./commands') if re.match(r'[^_].*\.py', f)]
loadModulesStep = 100 / len(loadModulesList)
loadProgress = 0


cmd = ''
for i in loadModulesList:
    try:
        className = i[:-3]
        mod = importlib.import_module('commands.%s' % className)
        cmd = getattr(mod, className.title())(commandConfig)
        modules.append(cmd)
    except ImportError as err:
        print('Error:', err, className)
    
    loadProgress += loadModulesStep
    stdout.write("\r" + 'Loading modules: {:.0%}'.format(loadProgress / 100))
    stdout.flush()
    time.sleep(0.01)
stdout.write('\n')

commandManager = command.manager.Manager(modules, commandConfig)

if not devMode:
    spl.logo_and_change_log_writer()

print('Cesvet Team AndrOS {}'.format(version))
print("")
print(commandConfig.get_text('start'))
print("")

color = command.color.Color()
# Command prompt
while not commandManager.get_quitFlag():
    path = commandManager.get_full_path()
    command = input(colored('[{}]> '.format(path), attrs=['bold']))
    com1 = command.split()
    if not com1:
        continue
    currentCommand = commandManager.parse_command(command)

    com = currentCommand.get_current_command()
    agvs = currentCommand.get_current_agvs()
    processedCount = 0
    for cmd in modules:
        # print(cmd.get_command())
        if com == cmd.get_command():
            print("")
            processedCount += 1
            cmd.answer(agvs, commandManager)
            print('')
    if processedCount == 0:
        color.print_error("{} - invalid command".format(com))

