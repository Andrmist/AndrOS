# import os
#
# class Users:
#
#     def __init__(self, commandManager, current_user):
#         self.users = commandManager.commandConfig.get_config['Usernames']
#         self.current_user = current_user
#         self.commandManager = commandManager
#
#
#     def set_user(self, username):
#         if self.current_user == 'root' or self.get_access(username) or self.current_user == username:
#             self.current_user = username
#         else:
#             return False
#
#     def reset_password(self, username, password):
#         if self.current_user == username or self.get_access(username) or self.current_user == 'root':
#             self.users[username] = password
#
#     def get_access(self, user):
#         while True:
#             password = input('Enter password for {}: '.format(user))
#             if password == 'quit':
#                 return False
#             elif password == commandManager.commandConfig.get_config['Users'][user]:
#                 self.current_user = user
#                 return True
#
#
#
#     def set_folder_for_user(self, user, folder_name):
#         try:
#             if self.current_user == user or self.get_access(user) or self.current_user == 'root':
#                 self.commandManager.commandConfig.get_config['User Folders'][user] = folder_name
#             else:
#                 return False
#         except FileExistsError:
#             self.commandManager.set_path('home')
#             os.mkdir(self.commandManager.get_full_path() + os.sep + folder_name)
#
#     def check_path(self, path):
#         # a = []
#         # for i in range(len(self.commandManager.path().split(os.sep))):
#         #     if self.commandManager.path().split(os.sep)[i] == 'home':
#         #         a.append(1)
#         #     for k in self.commandManager.commandConfig.get_config['User Folders']
