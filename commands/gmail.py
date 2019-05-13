import command.command
import command.email


class Gmail(command.command.Command):

    def answer(self, argvs ,commandManager):
        mail = command.email.Email(commandManager)
        try:
            if argvs[0] == '-s':
                mail.send(argvs[1], argvs[2], argvs[3])
        except IndexError:
            to = self.color.input_command('To: ')
            subject = self.color.input_command('Subject: ')
            message = self.color.input_command('Message: ')
            mail.send(to, message, subject)
