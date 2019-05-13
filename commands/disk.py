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
                self.color.print_error(errorText.format(disk))
                self.color.print_error(self.get_help().format(', '.join(commandManager.commandConfig.disks)))
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            self.color.print_error(errorText)
            self.write_help()