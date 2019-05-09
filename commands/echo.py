import command.command



class Echo(command.command.Command):

    def answer(self,agvs,commandManager):
        for i in agvs:
            print(i)
