import command.command
import os


class Cat(command.command.Command):

    def answer(self, agvs, commandManager):
        config = self.commandConfig.get_config()
        try:
            fileName = agvs[0]
            text = open(commandManager.get_full_path() + os.sep + fileName, 'r+').read()
            print(text)
        except FileNotFoundError:
            config = self.commandConfig.get_config()
            errorText = self.commandConfig.get_text("loadError").format(fileName)
            print(errorText)
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            print(errorText)
            self.write_help()