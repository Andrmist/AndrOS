import configparser
import codecs

class Config:
    def __init__(self, configFile):
        self.config_file = configFile
        self.config = configparser.ConfigParser()
        self.config.read_file(codecs.open(configFile, "r", "utf8"))
        self.disk = eval(self.config['DEFAULT']['diskslist'])[0]
        self.lang = self.config['DEFAULT']['lang'].upper()
        #conf = config[lang]

    def get_config(self):
        return self.config

    def get_lang(self):
        return self.lang

    def get_disk(self):
        return self.disk