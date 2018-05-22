import command.command
import os

class Start(command.command.Command):

    def answer(self,argvs,commandManager):
        fileName = argvs[0]
        try:
            os.system('py ' + commandManager.get_full_path() + os.sep + fileName)
        except FileNotFoundError:
            config = self.commandConfig.get_config()
            errorText = 'Load Error!'
            if self.commandConfig.config.has_option(self.lang, "loadError"):
                errorText = config[self.lang]["loadError"].format(fileName)
            print(errorText)
        except OSError:
            config = self.commandConfig.get_config()
            errorText = 'Load Error!'
            if self.commandConfig.config.has_option(self.lang, "loadError"):
                errorText = config[self.lang]["loadError"].format(fileName)
            print(errorText)
        except IndexError:
            errorText = 'Invalid Arguments!'
            if self.commandConfig.config.has_option(self.lang, "invalidArgument"):
                errorText = self.commandConfig.get_config()[self.lang]["invalidArgument"]
            print(errorText)
            self.write_help()