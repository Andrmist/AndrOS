import command.parser
import os

class Manager:
    def __init__(self,modules, commandConfig):
        self.modules = modules
        self.quitFlag = False
        self.commandConfig = commandConfig
        self.path = ''
        self.fullPathList = []

    def parse_command(self, command_str):
        self.current_command = command.parser.Parser(command_str)
        return self.current_command

    def get_modules(self):
        return self.modules

    def get_quitFlag(self):
        return self.quitFlag

    def quit(self):
        self.quitFlag = True

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def get_full_path(self):
        return 'disks' + os.sep + self.commandConfig.get_disk() + os.sep + self.path

    def is_path_exists(self, path):
        return os.path.exists('disks' + os.sep + self.commandConfig.get_disk() + os.sep + path)