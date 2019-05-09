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
                print(self.commandConfig.get_text("AndrOS Writer"))
                fullFileName = commandManager.get_full_path() + os.sep + fileName
                currentFile = open(fullFileName, 'w')
                currentText = input(self.commandConfig.get_text("typetext"))
                currentFile.write(currentText)
                currentFile.close()
            except OSError:
                # errorText = 'Write Error!'
                errorText = self.commandConfig.get_text("writeError").format(fileName)
                print(errorText)
        else:
            # errorText = 'Invalid Arguments!'

            errorText = self.commandConfig.get_text("invalidArgument")
            print(errorText)
            self.write_help()