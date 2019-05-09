import command.command
import os

class Start(command.command.Command):

    def answer(self,argvs,commandManager):
        try:
            fileName = argvs[0]
            os.system('py ' + commandManager.get_full_path() + os.sep + fileName)
        except FileNotFoundError and OSError:
            config = self.commandConfig.get_config()
            errorText = self.commandConfig.get_text("loadError").format(fileName)
            print(errorText)
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            print(errorText)
            self.write_help()