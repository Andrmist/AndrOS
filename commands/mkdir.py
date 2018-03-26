import command.command
import os

class Start(command.command.Command):

    def answer(self,argvs,commandManager):
        dirName = argvs[0]
        os.mkdir(dirName)