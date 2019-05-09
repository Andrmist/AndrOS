import command.command
import os

class Help(command.command.Command):

    def answer(self,agvs,commandManager):
        # print(commandManager.commandConfig.config[commandManager.commandConfig.get_lang()])
        if len(agvs) == 0:
            for cmd in commandManager.get_modules():
                helper = cmd.get_helper()
                if len(helper) > 0:
                    print(helper)
                else:
                    print(cmd.get_command())
        else:
            if agvs[0] == "rm":
                print(self.commandConfig.get_text("rmhelp"))