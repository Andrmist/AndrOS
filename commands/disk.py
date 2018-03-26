import command.command
import os


class Disk(command.command.Command):

    def answer(self,argvs,commandManager):
        disk = argvs[0]
        if commandManager.commandConfig.set_disk(disk):
            commandManager.set_path('')
            pass
        else:
            errorText = 'Invalid Disk Name!'
            if self.commandConfig.config.has_option(self.lang, "invalidDiskName"):
                errorText = commandManager.commandConfig.config[self.lang]["invalidDiskName"]
            print(errorText.format(disk))
            print(self.get_help().format(', '.join(commandManager.commandConfig.disks)))