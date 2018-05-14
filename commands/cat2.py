import command.command
import os

class Cat2(command.command.Command):

    def answer(self,agvs,commandManager):
        try:
            fileName = agvs[0]
            text = open(commandManager.get_full_path() + os.sep + fileName, 'r+').read()
            print(text)
        except FileNotFoundError:
            config = self.commandConfig.get_config()
            errorText = 'Load Error!'
            if self.commandConfig.config.has_option(self.lang, "loadError"):
                errorText = config[self.lang]["loadError"].format(fileName)
            print(errorText)