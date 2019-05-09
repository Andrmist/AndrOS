requires = ['requests']
import command.command
#import command.package_manager
import requests
import os
#pm = command.package_manager.PackageManager()


class Getcomm(command.command.Command):

    def answer(self, agvs, commandManager):
        if self.check_arguments(agvs):
            try:
                if agvs[0] == 'install':
                    if agvs[1] == '-r' or '-raw':
                        file_text = requests.get(agvs[2])
                        filename = agvs[2].split('/')[-1]
                        file = open('commands' + os.sep + filename, 'w')
                        file.write(file_text.text)
                        #pm.check_file(filename)
            except IndexError:
                print('Error')
