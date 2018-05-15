import command.command
import os
import time
import sys


class Reboot(command.command.Command):
    # It's a beta function.
    def answer(self,agvs,commandManager):
        print('Rebooting...')
        time.sleep(1)
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
