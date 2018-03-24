import configparser


try:
    if config['DEFAULT']['key'] == start.a:
        print('Key is tested...')
except NoSectionError:
    print('Oops. Sorry, but key does not exist:(. We are teleporting you to DEMO vesrion...')
    os.system('py AndrOSDemo.py')