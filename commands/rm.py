import command.command
import os
import shutil

class Rm(command.command.Command):

    def answer(self,argvs,commandManager):
        try:
            if argvs[0] == "-d":
                fileName = argvs[1]
                shutil.rmtree(commandManager.get_full_path() + os.sep + fileName)
            else:
                fileName = argvs[0]
                os.remove(commandManager.get_full_path() + os.sep + fileName)
        except FileNotFoundError and OSError:
            config = self.commandConfig.get_config()
            errorText = self.commandConfig.get_text("loadError").format(fileName)
            self.color.print_error(errorText)
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            self.color.print_error(errorText)
            self.write_help()
