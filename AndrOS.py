# -*- coding: utf-8 -*-
import time
import start
import configparser
import os

time.sleep(5)
print("""
Cesvet Team
       CCCCC     EEEEEE     SSSSSSSS     V         V     EEEEEE     TTTTTTTTT
       C         E          S             V       V      E              T
       C         EEEEEE     SSSSSSSS       V     V       EEEEEE         T
       C         E                 S        V   V        E              T
       C         E                 S         V V         E              T
       CCCCC     EEEEEE     SSSSSSSS          V          EEEEEE         T

STARTING THE MACHINE...
""")
time.sleep(5)

print('Starting AndrOS...')
time.sleep(2)
print('Loading files...')
for i in range(0, 100, 10):
    time.sleep(0.5)
    print('{}%'.format(i))


config = configparser.ConfigParser()
config.read('config.ini')
try:
    if config['DEFAULT']['key'] == start.a:
        print('Key is tested...')
except NoSectionError:
    print('Oops. Sorry, but key does not exist:(. We are teleporting you to DEMO vesrion...')
    os.system('py AndrOSDemo.py')

quitt = False
createdFile = None
currentFile = None
listOfCommands = ['quit', 'create', 'read', 'write', 'load', 'close', 'cd', 'help', 'print', 'disk', 'start', 'rm',
                  'mkdir']
listOfCommandsHelp = ['rm']
icon = '''                              tt%:                              
  .  . .  .  . .  .  . .  .  tt;tS:  . .  .  . .  .  . ;888X    
   .       .       .       ..%t;t;8 .      .       . X@S8 8888% 
     .  .    .  .    .  .   8;tS;t;X   . .    . .    88XSt; 8 8t
 .       .       .       . ;%t8;tttS..      .     . % @     .%S 
   .  .    .  .    .  .   .Xt%  S;t;8   .  .   .    8 .      88 
  .    .  .    .  .    .  Xt;tS  Xt;tX       .   . .. 8..     8t
    .       .       .    :S;ttX: ttt;S:  .            t%; :8X8 :
  .   . .    .  .    .   8;t8%t8  X;tt@   . .  .   .. ;8X888S   
    .     .    .  .    .%;tS. @t%  Xt;tS      .  .    ;t.888    
  .    .   .       .   .@t;%  .8S. ttt;X:  .        . %S88888   
     .   .   .  .    . 8;;S    .X8  X;t;8    . .      8% ;%;    
  .    .      .   .   ;;tX  .   :tS  S;ttS       .  .:.X %8     
    .     . .   .   . 8ttt   .  .@X: %t;tX: .  .      . 88X8@   
  .   .           .  Xt;% .    .  88  Xt;t8      .  . :.t:   X  
    .   . .  . .    .ttX   .      .%% .St;t%. .       S88 t88   
  .         .    .  8;tt .   .  .  SX. %;t;X.   .  .  88888.    
     . .  .    .   St;S       .     88  @;t;8        .          
  .          .    ;%;8  . . .    .   8X  8tt;@. . .          .  
    .  . . .    . 8;t: .       .   . :;. ;t;t;:     .         . 
  .           .  tt;8     .  .   .    88  @;tt8  .              
    . .  .  .   :St@ .  .      .    .  @X  @t;t8              . 
  .       .   . @t;;   .   . .    .    ;;. ;t;t;. .  .          
     . .       :%;8  .   .      .    .  88  8;tt8            .  
  .      . . ..@;%%t::;.    .      :::;t%tX .8;t;X .  .   .    .
    .  .      Xtt;t;;tt;t;;tt;;t;;t;t;t;tt;. ;t;t;.     .   .   
  .      .  ..S;S8888888888888888888888888X8  8;t;8  .    .   . 
    . .      8tt; .  .          .  .  .   .XX..@;ttX   .        
  .     .  .tt;8             .             :;. tt;t;;    .  .   
     .    . @;S:    .   .  .     .        . 88. 8;;t8  .     .  
  .    .   8;t%  .    .   .   .    . . .    .@X .@t;t8    .     
    .    .:;t8     .    .      .         .   t%..t;tttt     .  .
  .   .   8;tt  .    .     . .   . .  .   .   @8. 8t;tS; .      
    .   .8;t8 .   .    .  .            .    . t;S .Xt;tX.  .  . 
  .     %;t;.   .   .   .    . . .  .    .     @%. %t;t;8.      
     . ;St;8      .   .    .       .  .    .   Xt8  8t;t;X  .  .
  .   :St;t: . .    .    .    .  .      .    . .ttX .X;t;t8     
X888X%;t;t;tSX@8888SS; .    .       .;XS8888@XSt;ttSS%;t;t;%S@8@'''
command = ''
currentText = ''
currentFileName = ''
disk = eval(config['DEFAULT']['diskslist'])[0]

path = 'disks/' + disk
lang = config['DEFAULT']['lang'].upper()
conf = config[lang]
print(icon)
print(open('changelog.txt', 'r').read())

if config['DEFAULT']['lang'] == 'en':
    print('Cesvet Team AndrOS 0.7 Beta')
    print(conf['start'])
    while quitt != True:
        command = input(path + '>')
        command = command.split()
        if command[0] == listOfCommands[0]:
            quitt = True
        if command[0] == listOfCommands[1]:
            createdFile = open(path + '/' + command[1], 'x+')
            currentFile = createdFile
            createdFile = None
            currentFileName = command[1]
        if command[0] == listOfCommands[4]:
            try:
                currentFile = open(path + '/' + command[1], 'r+')
                currentFileName = command[1]
            except FileNotFoundError:
                print(conf['loadError'].format(command[1]))
        if command[0] == listOfCommands[2]:
            if currentFile == None:
                print(conf['noFilesLoad'])
            else:
                print(currentFile.read())
        if command[0] == listOfCommands[3]:
            if currentFile == None:
                print(conf['noFilesLoad'])
            else:
                print(conf['AndrOS Writer'])
                currentText = input(conf['typetext'])
                currentFile.write(currentText)
                currentFile = open(path + '/' + currentFileName, 'r+')
        if command[0] == listOfCommands[6]:
            if command[1] == '..':
                pathArr = (path.split('/'))[:-1]
                path = '/'.join(pathArr)
            else:
                path += '/' + command[1]
        if command[0] == listOfCommands[9]:
            for i in eval(config['DEFAULT']['diskslist']):
                if command[1] == i:
                    disk = i
                    path = 'disks/' + disk
                    break
        if command[0] == listOfCommands[8]:
            print(command[1])
        if command[0] == listOfCommands[10]:
            os.system('py ' + path + '/' + command[1])
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
        if command[0] == listOfCommands[7]:
            try:
                if command[1] == listOfCommandsHelp[0]:
                    print(conf['rmhelp'])
            except IndexError:
                print(conf['AndrOS Helper'])
