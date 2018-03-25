import configparser
import codecs

class Config:
    def __init__(self, configFile):
        self.config_file = configFile
        self.config = configparser.ConfigParser()
        self.config.read_file(codecs.open(configFile, "r", "utf8"))
        self.disks = eval(self.config['DEFAULT']['diskslist'])
        self.disk = disks[0]
        self.lang = self.config['DEFAULT']['lang'].upper()
        #conf = config[lang]

    def get_config(self):
        return self.config

    def get_lang(self):
        return self.lang

    def get_disk(self):
        return self.disk

    def set_disk(self, disk):
        if disk in self.disks:
            self.disk = disk
            return True
        return False