import command.command
import os
import os.path


class Cd(command.command.Command):

    def answer(self,argvs,commandManager):
        try:
            path = argvs[0]
            pathArr = path.split(os.sep)
            if commandManager.get_path() == '':
                currentPathArr  = []
            else:
                currentPathArr = (os.sep.split(commandManager.get_path()))
            # print(commandManager.get_path())
            # print(pathArr, currentPathArr)
            for i in range(len(pathArr)):
                if i == 0 and pathArr[i] == '':
                    currentPathArr = []
                    continue
                if pathArr[i] == '.':
                    continue
                if pathArr[i] == '..':
                    if len(currentPathArr):
                        currentPathArr.pop()
                    continue
                if pathArr[i] == '':
                    continue
                currentPathArr.append(pathArr[i])

            currentPath = os.sep.join(currentPathArr)
            if commandManager.is_path_exists(currentPath):
                commandManager.set_path(currentPath)
            else:
                print('Error')
        except IndexError:
            errorText = 'Invalid Arguments!'
            if self.commandConfig.config.has_option(self.lang, "invalidArgument"):
                errorText = self.commandConfig.get_config()[self.lang]["invalidArgument"]
            print(errorText)
            self.write_help()

            # if i == '..':
            #     if currentPathArr == '':
            #         pass
            #     else:
            #         pathArr = pathArr[:-1]
            # if i == '.':
            #     pass
            # if i != '..' or i != '.':
            #     if os.path.exists()
