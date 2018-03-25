class Command:
    def __init__(self, commandConfig):
        self.command = type(self).__name__.lower()
        self.commandConfig = commandConfig
        self.lang = commandConfig.get_lang()
        self.argvCount = 0

    def get_command(self):
        return self.command

    def get_helper(self):
        config = self.commandConfig.get_config()
        text = ''
        if self.commandConfig.config.has_option(self.lang, "helper " + self.command):
            text = config[self.lang]["helper " + self.command]
        return text

    def check_arguments(self, argvs):
        return (len(argvs) >= self.argvCount)

    def write_help(self):
        helper = self.get_helper()
        if len(helper) > 0:
            return helper