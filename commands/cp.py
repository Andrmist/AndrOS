import command.command
import os
from shutil import copyfile

class Cp(command.command.Command):

    def answer(self, agvs, commandManager):
        config = self.commandConfig.get_config()
        try:
            start_filename = agvs[0]
            end_filename = agvs[1]
            copyfile(commandManager.get_full_path() + os.sep + start_filename, commandManager.get_full_path() + os.sep + end_filename)
        except FileNotFoundError:
            errorText = self.commandConfig.get_text("loadError")
            self.color.print_error(errorText)
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            self.color.print_error(errorText)
            self.write_help()