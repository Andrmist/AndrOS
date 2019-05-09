import os
import configparser
import base64
import smtplib
import command.config

commandConfig = command.config.Config('config.json')
config = commandConfig.get_config()

pass_is_temp = False
email = ''
password = ''

if config['Options']['lang'] == '':
    print('''Welcome to AndrOS!
    You need to set settings for your Operating system
    Ласкаво просимо в AndrOS!
    Вам необхідно налаштувати Операційну систему''')
    disksList = []
    disk = ''
    disks = 0
    lang = ''
    select_params = False
    while not select_params:
        lang = input("Choose language for Operating system. Виеріть мову для Операційної системи. (en/uk):")
        if lang == "uk":
            disks = int(input(
                'Вкажіть кількість дисків (Вони будуть створені у "<папка с ОС>/disks"):'))
            # 'Укажите количество дисков(Они должны быть созданы в папке Операционной системы: Папка с ОС/disks):'
            for i in range(disks):
                if i == 0:
                    disk = input('Введіть назву головного диску(Наприклад: "C"):')
                    disksList.append(disk)
                # Название главного диска(папки с диском):'
                else:
                    disk = input(
                        'Вкажіть назву диску №' + str(i + 1) + '(Наприклад: "D"):')
                    disksList.append(disk)
            gmail_confirm = input('Гаразд. Чи бажаєте ви відправляти пошту через Gmail?(y/n): ')
            if gmail_confirm == 'y' or gmail_confirm == 'Y':
                print('''Введіть адрресу та пароль до Gmail акаунту
                    Увага! Ми не використовуємо і нікуди не пересилаєм ваші персональні дані
                            Ви можете змінити пошту та пароль у секції "Email" конфігураційного файлу.''')
                while True:
                    email = input('Вкажіть адрес Gmail(Введіть "exit", щоб закінчити): ')
                    if email == 'exit':
                        break
                    password = input('Вкажіть пароль(Введіть "exit", щоб закінчити): ')
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
            select_params = True
        elif lang == 'en':
            disks = int(input('Specify the number of disks (They should be created in the folder of the Operating system: OS folder/dist/disks):'))
                #'Укажите количество дисков(Они должны быть созданы в папке Операционной системы: Папка с ОС/dist/disks):'
            for i in range(disks):
                if i == 0:
                    disk = input('Enter name of main disk(For example: "C"):')
                    disksList.append(disk)
                #Название главного диска(папки с диском):'
                else:
                    disk = input('Enter name of disk №' + str(i + 1) + '(For example: "D"):')
                    disksList.append(disk)
            gmail_confirm = input('Good. You want to use Gmail in AndrOS?(y/n): ')
            if gmail_confirm == 'y' or gmail_confirm == 'Y':
                print('''Well, type email and password of Gmail account
                Warning! We do not in any way use your data except Google authorization
                        You can then change these settings in config file in the "Email" section.''')
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
            select_params = True
        else:
            continue

    disksListString = ''
    for i in disksList:
        disksListString += i + ' '
    config['Options'] = {
        'lang': lang,
        'disksList': disksList
    }
    config['Email']['email'] = email
    config['Email']['password'] = password
    commandConfig.save(config)
