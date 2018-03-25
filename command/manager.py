import command.parser

class Manager:
    def __init__(self,modules):
        self.modules = modules

    def parse_command(self,command_str):
        self.current_command = command.parser.Parser(command_str)
        return self.current_command

    def get_modules(self):
        return self.modules