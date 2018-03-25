import command.command
import os

class Touch(command.command.Command):

    def answer(self,agvs,commandManager):
        fileName = agvs[0]
        createdFile = open(commandManager.get_full_path() + os.sep + fileName, 'w')
        createdFile.close()