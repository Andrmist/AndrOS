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
time.sleep(1)
print('0%')
time.sleep(0.5)
print('10%')
time.sleep(0.5)
print('20%')
time.sleep(0.5)
print('30%')
time.sleep(0.5)
print('40%')
time.sleep(0.5)
print('50%')
time.sleep(0.5)
print('60%')
time.sleep(0.5)
print('70%')
time.sleep(0.5)
print('80%')
time.sleep(0.5)
print('90%')
time.sleep(0.5)
print('100%')
time.sleep(0.5)


config = configparser.ConfigParser()
config.read('config.ini')

quitt = False
createdFile = None
currentFile = None
listOfCommands = ['quit', 'create', 'read', 'write', 'load', 'close', 'cd', 'help', 'print', 'disk', 'start']
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
changeLogEN = '''Version 0.6:
—Deleted commands: "close"
—Added commands: "cd", "print", "disk"
—Added Setup OS
—Added Change Log
—Added Icon
This Update is not updated for ru version:(
To change language to english you must open config.ini and change value of lang:
It was: lang = ru
It becomes: lang = en
This will be updated in version 0.6.1 
--------------------------------------------------------
Version 0.5
—AndrOS was redone under Python 3
—Added russian language
'''
command = ''
currentText = ''
currentFileName = ''
disk = eval(config['DEFAULT']['diskslist'])[0]

path = 'disks/' + disk

print(icon)
print(changeLogEN)
if config['DEFAULT']['lang'] == 'en':
    print('Cesvet Team AndrOS 0.6')
    print('Type "help" for more information')
    while quitt != True:
        command = input(path + ':>')
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
                print('Load Error: "{}" is not found'.format(command[1]))
        if command[0] == listOfCommands[2]:
            if currentFile == None:
                print('No files is load!')
            else:
                print(currentFile.read())
        if command[0] == listOfCommands[3]:
            if currentFile == None:
                print('No files is load!')
            else:
                print("AndrOS Writer v. 0.1\n To save text, you have to press ENTER")
                currentText = input("Type your text here:\n")
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
        # if command[0] == listOfCommands[10]:
        #     subprocess.Popen(['py', currentFileName])
        if command[0] == listOfCommands[7]:
            print('''
            AndrOS Helper version 1.3
            quit - Quit from AndrOS
            create [file] - Create file
            read - Read (display) the contents of the file
            write - Open AndrOS Writer
            load [file] - Load file
            print [text or number] - Print the text or number (unfortunately, at the moment this command cannot perform numeric operations, this is due to the version of Python, namely version 3)
            cd [folder] - Go to folder. If you want to go back: cd ..
            help - Help
            disk [name of disk] - Go to the disk
            !start [python file] - Start Python file(py)
            ! - Work in Progress
            ''')
else:
    print('Cesvet Team AndrOS 0.5')
    print('Напишите "help" для получения дополнительной информации')
    # while quitt != True:
    #     command = input('C:/>')
    #
    #     if command == listOfCommands[0]:
    #         quitt = True
    #     if command[:6] == listOfCommands[1]:
    #         createdFile = open(command[7:], 'x')
    #         currentFile = createdFile
    #         createdFile = None
    #     if command[:4] == listOfCommands[4]:
    #         currentFile = open(command[5:], 'a')
    #     if command[:4] == listOfCommands[2]:
    #         if currentFile == None:
    #             print('Ни один файл не загружен!')
    #         else:
    #             print(currentFile.read())
    #     if command[:5] == listOfCommands[3]:
    #         if currentFile == None:
    #             print("Ни один файл не загружен!")
    #         else:
    #             print(
    #             "AndrOS Writer v. 0.1\nЕсли вы хотите перейти на новую строку, напишите там где должен быть переход: '\\n'. Чтобы сохранить текст в загруженом файле, нажмите ENTER")
    #             currentText = input("Введите текст здесь:\n")
    #             currentFile.write(currentText)
    #     if command[:5] == listOfCommands[5]:
    #         currentFile.close()
    #         currentFile = None
    #     if command[:4] == listOfCommands[7]:
    #         print('''
    #         AndrOS Helper версия 1.0
    #         quit - Выйти с AndrOS
    #         create [файл] - Создать файл
    #         read - Прочитать(вывести) содержимое файла
    #         write - Открыть AndrOS Writer
    #         load [файл] - Загрузить файл
    #         close - Закрыть файл
    #         ''')
    while quitt != True:
        command = input('C:/>')
        command.split()
        if command[0] == listOfCommands[0]:
            quitt = True
        if command[0] == listOfCommands[1]:
            createdFile = open(command[1], 'x')
            currentFile = createdFile
            createdFile = None
        if command[0] == listOfCommands[4]:
            currentFile = open(command[1], 'a')
        if command[0] == listOfCommands[2]:
            if currentFile == None:
                print('Ни один файл не загружен!')
            else:
                print(currentFile.read())
        if command[0] == listOfCommands[3]:
            if currentFile == None:
                print('Ни один файл не загружен!')
            else:
                print("AndrOS Writer v. 0.1\nЕсли вы хотите перейти на новую строку, напишите там где должен быть переход: '\\n'. Чтобы сохранить текст в загруженом файле, нажмите ENTER")
                currentText = input("Введите текст здесь:\n")
                currentFile.write(currentText)
        if command[0] == listOfCommands[5]:
            currentFile.close()
            currentFile = None
        if command[0] == listOfCommands[7]:
            print('''
            AndrOS Helper версия 1.1
            quit - Выйти с AndrOS
            create [файл] - Создать файл
            read - Прочитать(вывести) содержимое файла
            write - Открыть AndrOS Writer
            load [файл] - Загрузить файл
            close - Закрыть файл
            print [текст или число] - Вывести текст или число(к сожалению, на данный момент эта команда не может выполнять числовые операции, связано это с версией Python, а именно 3 версия)
            cd [папка] - Перейти в папку, которая лежит в данном пути, чтобы перейти назад: cd ..
            help - Справка
            disk [название диска] - Перейти на диск
            ''')