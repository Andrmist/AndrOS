import command.command
import os

class Ls(command.command.Command):

    def answer(self,agvs,commandManager):
        for i in os.listdir(commandManager.get_full_path()):
            print(i)