class Parser:
    def __init__(self,command_str):
        words = command_str.split()
        self.command = words.pop(0)
        self.agvs = words

    def get_current_command(self):
        return self.command

    def get_current_agvs(self):
        return self.agvs
