class Command:
    def __init__(self, config, lang):
        self.command = type(self).__name__.lower()
        self.config = config
        self.lang = lang

    def get_command(self):
        return self.command