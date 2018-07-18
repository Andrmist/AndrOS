import os
import configparser
import base64
import smtplib

config = configparser.ConfigParser()
config.read('config.ini')

pass_is_temp = False
email = ''
password = ''

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
        gmail_confirm = input('Хорошо. Вы хотите пользоваться почтой Gmail в AndrOS?(y/n): ')
        if gmail_confirm == 'y' or gmail_confirm == 'Y':
            print('''Тогда введите данные Gmail почты.
            Внимание! Мы не в коем случае не используем ваши данные кроме как авторизации Google
            Можно потом изменить эти настройки в config.ini в секции [Email]''')
            while True:
                email = input('Введите електронную почту("exit" чтобы вийти): ')
                if email == 'exit':
                    break
                password = input('Введите пароль("exit" чтобы вийти): ')
                if password == 'exit':
                    break
                print('Авторизуемся...')
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    break
                except smtplib.SMTPAuthenticationError:
                    print('Ошибка авторизации!')
                    continue
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
            gmail_confirm = input('Good. You want to use Gmail in AndrOS?(y/n): ')
            if gmail_confirm == 'y' or gmail_confirm == 'Y':
                print('''Well, type email and password of Gmail account
                Warning! We do not in any way use your data except Google authorization
                You can then change these settings in config.ini in the [Email] section.''')
                while True:
                    email = input('Enter your email("exit" to exit): ')
                    if email == 'exit':
                        break
                    password = input('Enter password("exit" to exit): ')
                    if password == 'exit':
                        break
                    print('Authorizing...')
                    try:
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        break
                    except smtplib.SMTPAuthenticationError:
                        print('Error!')
                        continue
    disksListString = ''
    for i in disksList:
        disksListString += i + ' '
    config['DEFAULT'] = {
        'lang': lang,
        'disksList': disksList
    }
    config['Email']['email'] = email
    config['Email']['password'] = password
    with open('config.ini', 'w') as configfile:
        config.write(configfile)