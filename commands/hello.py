class Hello:
    def __init__(self):
        self.command = 'hello'

    def get_command(self):
        return self.command

    def answer(self,agvs,commandManager):
        print("World")
