class Echo:
    def __init__(self):
        self.command = 'echo'

    def get_command(self):
        return self.command

    def answer(self,agvs,commandManager):
        for i in agvs:
            print(i)
