import command.command
import os
import sys
import re
from colorama import init
from termcolor import colored

class Ls(command.command.Command):

    def answer(self, agvs, commandManager):
        try:
            if agvs[0] == '-s':
                for i in os.listdir(commandManager.get_full_path()):
                    if os.path.isdir(commandManager.get_full_path() + os.sep + i):
                        self.color.print_dir('/' + i + "  " + str(os.path.getsize(commandManager.get_full_path() + os.sep + i)))
                    else:
                        if re.match(r'[^_].*\.py', i):
                            self.color.print_py(i + "  " + str(os.path.getsize(commandManager.get_full_path() + os.sep + i)))
                        elif i[0] == '.':
                            self.color.print_inv(i + "  " + str(os.path.getsize(commandManager.get_full_path() + os.sep + i)))
                        else:    
                            print(i + "  " + str(os.path.getsize(commandManager.get_full_path() + os.sep + i)))
        except IndexError:
            for i in os.listdir(commandManager.get_full_path()):
                if os.path.isdir(commandManager.get_full_path() + os.sep + i):
                    self.color.print_dir('/' + i)
                else:
                    if re.match(r'[^_].*\.py', i):
                            self.color.print_py(i)
                    elif i[0] == '.':
                        self.color.print_inv(i)
                    else:
                        print(i)
