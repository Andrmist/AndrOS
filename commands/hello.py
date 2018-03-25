import command.command

class Hello(command.command.Command):

    def answer(self,agvs,commandManager):
        print("World")
