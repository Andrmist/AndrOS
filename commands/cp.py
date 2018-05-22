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
            print('File not found!')
        except IndexError:
            errorText = 'Invalid Arguments!'
            if self.commandConfig.config.has_option(self.lang, "invalidArgument"):
                errorText = config[self.lang]["invalidArgument"]
            print(errorText)
            self.write_help()