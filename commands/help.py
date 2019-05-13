import command.command
import os

class Help(command.command.Command):

    def answer(self,agvs,commandManager):
        # print(commandManager.commandConfig.config[commandManager.commandConfig.get_lang()])
        if len(agvs) == 0:
            for cmd in commandManager.get_modules():
                helper = cmd.get_helper()
                if len(helper) > 0:
                    self.color.print_info(helper)
                else:
                    self.color.print_info(cmd.get_command())
        else:
            if agvs[0] in self.commandConfig.get_config()["Localization"][self.commandConfig.get_lang()]["Help"]:
                self.color.print_info(self.commandConfig.get_config()["Localization"][self.commandConfig.get_lang()]["Help"][agvs[0]])
