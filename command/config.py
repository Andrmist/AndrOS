import json
import codecs

class Config:
    def __init__(self, configFile):
        self.config_file = configFile
        with codecs.open(self.config_file, encoding='utf-8') as jsonF:
            self.config = json.load(jsonF)
        self.disks = self.config["Options"]["disksList"]
        self.disk = self.disks[0]
        self.lang = self.config['Options']['lang'].upper()
        #conf = config[lang]

    def get_config(self):
        return self.config

    def get_lang(self):
        return self.lang

    def get_disk(self):
        return self.disk

    def get_text(self, key):
        if key in self.config["Localization"][self.lang]:
            return self.config["Localization"][self.lang][key]
        else:
            if key in self.config["Localization"]["EN"]:
                return self.config["Localization"]["EN"][key]
            else:
                return ""

    def set_disk(self, disk):
        if disk in self.disks:
            self.disk = disk

            return True
        return False

    def get_version(self):
        return self.config["Options"]["version"]

    def save(self, data):
        with open(self.config_file, "w") as jsonWF:
            json.dump(data, indent=4, fp=jsonWF, ensure_ascii=False)

