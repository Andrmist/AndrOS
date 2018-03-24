import os
import configparser
import base64

isKey = False
a = ''
with open('key.txt', 'r+') as file:
    a = base64.standard_b64decode(file.read())
a = a.decode('utf-8')

config = configparser.ConfigParser()
config.read('config.ini')

if config['DEFAULT']['lang'] == '':
    print('''Welcome to AndrOS!
    You need to set settings for your Operating system
    Добро пожаловать в AndrOS!
    Вам необходимо настроить Операционую систему''')
    disksList = []
    disk = ''
    disks = 0
    lang = input("Choose language for Operating system. Выберите язык для вашей операционной системы. (en/ru):")
    if lang == 'ru':
        disks = int(input('Укажите количество дисков(Они должны быть созданы в папке Операционной системы: Папка с ОС/dist/disks):'))
        for i in range(disks):
            if i == 0:
                disk = input('Название главного диска(папка главного диска: Папка с ОС/dist/disks):')
            else:
                disk = input('Название диска №' + str(i + 1) + '(папка диска: Папка с ОС/dist/disks):')
            disksList.append(disk)
        print('''Замечательно. Теперь когда все готово, введите ключ, который шёл к установщику. 
        Если вы загрузили ДЕМО версию, и у вас нету ключа, пожайлуста, оставте поле ввода пустым''')
        while isKey is None:
            keyinput = input('Ключ Активации:')
            if keyinput == a:
                isKey = True
                print('Верно!')
            elif keyinput != '':
                print('Введенный код неверный! Пожайлуста повторите попытку')
            else:
                isKey = False


    else:
            disks = int(input('Specify the number of disks (They should be created in the folder of the Operating system: OS folder/dist/disks):'))
                #'Укажите количество дисков(Они должны быть созданы в папке Операционной системы: Папка с ОС/dist/disks):'
            for i in range(disks):
                if i == 0:
                    disk = input('Enter name of main disk(folder of main disk in folder: OS folder/dist/disks):')
                #Название главного диска(папки с диском):'
                else:
                    disk = input('Enter name of disk №' + str(i + 1) + '(folder of main disk in folder: OS folder/dist/disks):')
                    disksList.append(disk)
            print('''Very good! Now when everything is ready, enter the key that went to the installer. 
            If you downloaded the DEMO version, and you do not have the key, please leave the input field empty''')
            while isKey is None:
                    keyinput = input('Ключ Активации:')
                    if keyinput == a:
                        isKey = True
                        print('Верно!')
                    elif keyinput != '':
                        print('Введенный код неверный! Пожайлуста повторите попытку')
                    else:
                        isKey = False
    disksListString = ''
    if isKey is True:
        for i in disksList:
            disksListString += i + ' '
        config['DEFAULT'] = {
            'lang': lang,
            'disksList': disksList,
            'key': a
        }
    else:
        for i in disksList:
            disksListString += i + ' '
        config['DEFAULT'] = {
            'lang': lang,
            'disksList': disksList
        }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)