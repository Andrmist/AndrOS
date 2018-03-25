# -*- coding: utf-8 -*-
import time
import start
import configparser
import os
import re
import importlib
from sys import stdout
import splash
import codecs
import command.manager
import command.config


version = '0.8.0 Beta'
devMode = ('DEV' in os.environ) if True else False

commandConfig = command.config.Config('config.ini')
disk = commandConfig.get_disk()
lang = commandConfig.get_lang()
config = commandConfig.get_config()
conf = config[lang]

spl = splash.Splash()
if not devMode:
    spl.header_screen_writer()

modules = []
loadModulesList = [f for f in os.listdir('./commands') if re.match(r'[^_].*\.py', f)]
loadModulesStep = 100 / len(loadModulesList)
loadProgress = 0

for i in loadModulesList:
    try:
        className = i[:-3]
        mod = importlib.import_module('commands.%s' % className)
        cmd = getattr(mod, className.title())(config, lang)
        modules.append(cmd)
    except ImportError as err:
        print('Error:', err)
    loadProgress += loadModulesStep
    stdout.write("\r{}%".format(loadProgress))
    stdout.flush()
    time.sleep(0.1)
stdout.write('\n')

commandManager = command.manager.Manager(modules)

if not devMode:
    spl.logo_and_change_log_writer()

# quitFlag = False
# createdFile = None
# currentFile = None
# listOfCommands = ['quit', 'create', 'read', 'write', 'load', 'close',
#                   'cd', 'help', 'print', 'disk', 'start', 'rm', 'mkdir', 'ls']
# listOfCommandsHelp = ['rm']
# command = ''
# currentText = ''
# currentFileName = ''

path = 'disks/' + disk


print('Cesvet Team AndrOS {}'.format(version))
print(conf['start'])

while not commandManager.get_quitFlag():
    command = input(path + '>')
    currentCommand = commandManager.parse_command(command)

    com = currentCommand.get_current_command()
    agvs = currentCommand.get_current_agvs()

    for cmd in modules:
        # print(cmd.get_command())
        if com == cmd.get_command():
            cmd.answer(agvs, commandManager)

    # command = command.split()
    # # quit
    # if command[0] == listOfCommands[0]:
    #     quitFlag = True
    # # create
    # if command[0] == listOfCommands[1]:
    #     createdFile = open(path + '/' + command[1], 'x+')
    #     currentFile = createdFile
    #     createdFile = None
    #     currentFileName = command[1]
    # # load
    # if command[0] == listOfCommands[4]:
    #     try:
    #         currentFile = open(path + '/' + command[1], 'r+')
    #         currentFileName = command[1]
    #     except FileNotFoundError:
    #         print(conf['loadError'].format(command[1]))
    # # read
    # if command[0] == listOfCommands[2]:
    #     if currentFile == None:
    #         print(conf['noFilesLoad'])
    #     else:
    #         print(currentFile.read())
    # # write
    # if command[0] == listOfCommands[3]:
    #     if currentFile == None:
    #         print(conf['noFilesLoad'])
    #     else:
    #         print(conf['AndrOS Writer'])
    #         currentText = input(conf['typetext'])
    #         currentFile.write(currentText)
    #         currentFile = open(path + '/' + currentFileName, 'r+')
    # # cd
    # if command[0] == listOfCommands[6]:
    #     if command[1] == '..':
    #         pathArr = (path.split('/'))[:-1]
    #         path = '/'.join(pathArr)
    #     else:
    #         path += '/' + command[1]
    # # disk
    # if command[0] == listOfCommands[9]:
    #     for i in eval(config['DEFAULT']['diskslist']):
    #         if command[1] == i:
    #             disk = i
    #             path = 'disks/' + disk
    #             break
    # # print
    # if command[0] == listOfCommands[8]:
    #     print(command[1])
    # # start
    # if command[0] == listOfCommands[10]:
    #     os.system('py ' + path + '/' + command[1])
    # # mkdir
    # if command[0] == listOfCommands[12]:
    #     os.mkdir(path + '/' + command[1])
    # if command[0] == listOfCommands[11]:
    #     if len(command) == 1:
    #         print(conf['rmhelp'])
    #     else:
    #         try:
    #             if command[1] == '-d' and command[2] != '':
    #                 os.rmdir(path + '/' + command[2])
    #         except IndexError:
    #             os.remove(path + '/' + command[1])
    # # ls
    # if command[0] == listOfCommands[13]:
    #     for i in os.listdir(path):
    #         print(i)
    # # help
    # if command[0] == listOfCommands[7]:
    #     try:
    #         if command[1] == listOfCommandsHelp[0]:
    #             print(conf['rmhelp'])
    #     except IndexError:
    #         print(conf['AndrOS Helper'])
