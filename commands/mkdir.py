import command.command
import os

class Mkdir(command.command.Command):

    def answer(self,argvs,commandManager):
        try:
            dirName = argvs[0]
            os.mkdir(commandManager.get_full_path() + os.sep + dirName)
        except IndexError:
            errorText = 'Invalid Arguments!'
            if self.commandConfig.config.has_option(self.lang, "invalidArgument"):
                errorText = self.commandConfig.get_config()[self.lang]["invalidArgument"]
            print(errorText)
            self.write_help()