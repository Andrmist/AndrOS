import command.command
import os

class Write(command.command.Command):

    def __init__(self, commandConfig):
        command.command.Command.__init__(self, commandConfig)
        self.argvCount = 1

    def answer(self,argvs,commandManager):
        config = self.commandConfig.get_config()
        if self.check_arguments(argvs):
            try:
                fileName = argvs[0]
                print(config[self.lang]['AndrOS Writer'])
                fullFileName = commandManager.get_full_path() + os.sep + fileName
                currentFile = open(fullFileName, 'w')
                currentText = input(config[self.lang]['typetext'])
                currentFile.write(currentText)
                currentFile.close()
            except OSError:
                errorText = 'Write Error!'
                if self.commandConfig.config.has_option(self.lang, "writeError"):
                    errorText = config[self.lang]["writeError"].format(fileName)
                print(errorText)
        else:
            errorText = 'Invalid Arguments!'
            if self.commandConfig.config.has_option(self.lang, "invalidArgument"):
                errorText = config[self.lang]["invalidArgument"]
            print(errorText)
            self.write_help()