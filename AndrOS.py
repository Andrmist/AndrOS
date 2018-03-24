# -*- coding: utf-8 -*-
import time
import start
import configparser
import os
import splash
import codecs

version = '0.7.1 Beta'
devMode = ('DEV' in os.environ) if True else False

config = configparser.ConfigParser()
config.read_file(codecs.open("config.ini", "r", "utf8"))

spl = splash.Splash()
if not devMode:
    spl.header_screen_writer()
    spl.logo_and_change_log_writer()

quitFlag = False
createdFile = None
currentFile = None
listOfCommands = ['quit', 'create', 'read', 'write', 'load', 'close',
                  'cd', 'help', 'print', 'disk', 'start', 'rm', 'mkdir', 'ls']
listOfCommandsHelp = ['rm']
command = ''
currentText = ''
currentFileName = ''
disk = eval(config['DEFAULT']['diskslist'])[0]

path = 'disks/' + disk
lang = config['DEFAULT']['lang'].upper()
conf = config[lang]


print('Cesvet Team AndrOS {}'.format(version))
print(conf['start'])
while quitFlag != True:
    command = input(path + '>')
    command = command.split()
    # quit
    if command[0] == listOfCommands[0]:
        quitFlag = True
    # create
    if command[0] == listOfCommands[1]:
        createdFile = open(path + '/' + command[1], 'x+')
        currentFile = createdFile
        createdFile = None
        currentFileName = command[1]
    # load
    if command[0] == listOfCommands[4]:
        try:
            currentFile = open(path + '/' + command[1], 'r+')
            currentFileName = command[1]
        except FileNotFoundError:
            print(conf['loadError'].format(command[1]))
    # read
    if command[0] == listOfCommands[2]:
        if currentFile == None:
            print(conf['noFilesLoad'])
        else:
            print(currentFile.read())
    # write
    if command[0] == listOfCommands[3]:
        if currentFile == None:
            print(conf['noFilesLoad'])
        else:
            print(conf['AndrOS Writer'])
            currentText = input(conf['typetext'])
            currentFile.write(currentText)
            currentFile = open(path + '/' + currentFileName, 'r+')
    # cd
    if command[0] == listOfCommands[6]:
        if command[1] == '..':
            pathArr = (path.split('/'))[:-1]
            path = '/'.join(pathArr)
        else:
            path += '/' + command[1]
    # disk
    if command[0] == listOfCommands[9]:
        for i in eval(config['DEFAULT']['diskslist']):
            if command[1] == i:
                disk = i
                path = 'disks/' + disk
                break
    # print
    if command[0] == listOfCommands[8]:
        print(command[1])
    # start
    if command[0] == listOfCommands[10]:
        os.system('py ' + path + '/' + command[1])
    # mkdir
    if command[0] == listOfCommands[12]:
        os.mkdir(path + '/' + command[1])
    if command[0] == listOfCommands[11]:
        if len(command) == 1:
            print(conf['rmhelp'])
        else:
            try:
                if command[1] == '-d' and command[2] != '':
                    os.rmdir(path + '/' + command[2])
            except IndexError:
                os.remove(path + '/' + command[1])
    # ls
    if command[0] == listOfCommands[13]:
        for i in os.listdir(path):
            print(i)
    # help
    if command[0] == listOfCommands[7]:
        try:
            if command[1] == listOfCommandsHelp[0]:
                print(conf['rmhelp'])
        except IndexError:
            print(conf['AndrOS Helper'])
