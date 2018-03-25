import command.command
import os

class Disk(command.command.Command):

    def answer(self,argvs,commandManager):
        disk = argvs[0]
        if commandManager.commandConfig.set_disk(disk):
            commandManager.set_path('')
        else:
            errorText = 'Invalid Disk Name!'
            if self.commandConfig.config.has_option(self.lang, "invalidDiskName"):
                errorText = config[self.lang]["invalidDiskName"]
            print(errorText)
            print(self.write_help().format())