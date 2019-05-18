from colorama import Fore, Back, Style
import colorama
from termcolor import colored


class Color:

    def __init__(self):
        colorama.init()

    def print_error(self, text):
        print("!", Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)

    def print_info(self, text):
        print("?", Fore.CYAN + text + Style.RESET_ALL)

    def print_command(self, text):
        print("\033[1;33;40m {} \033[0m".format(text))

    def input_command(self, text):
        rez = input(colored('[{}]'.format(text), 'grey', "on_green"))
        return rez
    
    def print_dir(self, text):
        print(Fore.BLUE + Style.BRIGHT + text + Style.RESET_ALL)

    def print_py(self, text):
        print(Fore.GREEN + Style.BRIGHT + text + Style.RESET_ALL)

    def print_inv(self, text):
        print("\033[1;30;40m{} \033[0m".format(text))
