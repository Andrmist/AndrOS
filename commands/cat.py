import command.command
import os


class Cat(command.command.Command):

    def answer(self, agvs, commandManager):
        config = self.commandConfig.get_config()
        fileName = agvs[0]
        try:
            text = open(commandManager.get_full_path() + os.sep + fileName, 'r+').read()
            print(text)
        except FileNotFoundError:
            config = self.commandConfig.get_config()
            errorText = 'Load Error!'
            if self.commandConfig.config.has_option(self.lang, "loadError"):
                errorText = config[self.lang]["loadError"].format(fileName)
            print(errorText)
        except IndexError:
            errorText = 'Invalid Arguments!'
            if self.commandConfig.config.has_option(self.lang, "invalidArgument"):
                errorText = config[self.lang]["invalidArgument"]
            print(errorText)
            self.write_help()