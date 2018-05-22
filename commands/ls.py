import command.command
import os
import sys

class Ls(command.command.Command):

    def answer(self,agvs,commandManager):
        try:
            if agvs[0] == '-s':
                for i in os.listdir(commandManager.get_full_path()):
                    print(i, '', '', os.path.getsize(commandManager.get_full_path() + os.sep + i))
        except IndexError:
            for i in os.listdir(commandManager.get_full_path()):
                print(i)