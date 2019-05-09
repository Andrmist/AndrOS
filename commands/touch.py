import command.command
import os


class Touch(command.command.Command):

    def answer(self, agvs, commandManager):
        config = self.commandConfig.get_config()
        try:
            fileName = agvs[0]
            createdFile = open(commandManager.get_full_path() + os.sep + fileName, 'w')
            createdFile.close()
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            print(errorText)
            self.write_help()
