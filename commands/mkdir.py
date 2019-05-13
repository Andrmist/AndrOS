import command.command
import os

class Mkdir(command.command.Command):

    def answer(self,argvs,commandManager):
        try:
            dirName = argvs[0]
            os.mkdir(commandManager.get_full_path() + os.sep + dirName)
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            self.color.print_error(errorText)
            self.write_help()