import command.command

class Quit(command.command.Command):

    def answer(self,agvs,commandManager):
        print('Shut down...')
        commandManager.quit()