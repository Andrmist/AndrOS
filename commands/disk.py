import command.command
import os


class Disk(command.command.Command):

    def answer(self,argvs,commandManager):
        try:
            disk = argvs[0]
            if commandManager.commandConfig.set_disk(disk):
                commandManager.set_path('')
                pass
            else:
                errorText = self.commandConfig.get_text("invalidDiskName")
                print(errorText.format(disk))
                print(self.get_help().format(', '.join(commandManager.commandConfig.disks)))
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            print(errorText)
            self.write_help()