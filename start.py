# -*- coding: utf-8 -*-
import os
import configparser
import base64
import smtplib
import command.config
import tkinter as tk
from tkinter import filedialog

commandConfig = command.config.Config('config.json')
config = commandConfig.get_config()

pass_is_temp = False
email = ''
password = ''

if config['Options']['lang'] == '':
    print('''Welcome to AndrOS!
    You need to set settings for your Operating system
    Ласкаво просимо в AndrOS!
    Вам необхiдно налаштувати Операцiйну систему''')
    disksList = []
    disk = ''
    disks = 0
    lang = ''
    select_params = False
    while not select_params:
        lang = input("Choose language for Operating system. Виберiть мову для Операцiйної системи. (en/uk):")
        if lang == "uk":
            disks = int(input(
                'Вкажiть кiлькiсть дискiв (Вони будуть створенi у "<папка с ОС>/disks"):'))
            # 'Укажите количество дисков(Они должны быть созданы в папке Операционной системы: Папка с ОС/disks):'
            for i in range(disks):
                if i == 0:
                    root = tk.Tk()
                    root.withdraw()
                    dirname = filedialog.askdirectory(title='Введiть папку головного диску:')
                    dir = dirname.split("/")
                    disksList.append(dir[-1])
                # Название главного диска(папки с диском):'
                else:
                    root = tk.Tk()
                    root.withdraw()
                    dirname = filedialog.askdirectory(title='Вкажiть папку диску №' + str(i + 1) + ':')
                    dir = dirname.split("/")
                    disksList.append(dir[-1])
            gmail_confirm = input('Гаразд. Чи бажаєте ви вiдправляти пошту через Gmail?(y/n): ')
            if gmail_confirm == 'y' or gmail_confirm == 'Y':
                print('''Введiть адресу та пароль до Gmail акаунту
                    Увага! Ми не використовуємо i нiкуди не пересилаєм вашi персональнi данi
                            Ви можете змiнити пошту та пароль у секцiї "Email" конфiгурацiйного файлу.''')
                while True:
                    email = input('Вкажiть адрес Gmail(Введiть "exit", щоб закiнчити): ')
                    if email == 'exit':
                        break
                    password = input('Вкажiть пароль(Введiть "exit", щоб закiнчити): ')
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
    config['Options']['lang'] = lang
    config['Options']['disksList'] = disksList
    
    config['Email']['email'] = email
    config['Email']['password'] = password
    commandConfig.save(config)
