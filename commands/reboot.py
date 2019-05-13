import command.command
import os
import time
import sys


class Reboot(command.command.Command):
    # It's a beta function.
    def answer(self,agvs,commandManager):
        self.color.print_command('Rebooting...')
        time.sleep(1)
        filename = sys.argv[0]
        os.system(sys.executable + ' ' + filename)

        sys.exit(0)
