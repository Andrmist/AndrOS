import command.command

class Italent(command.command.Command):
    def answer(self, agvs, commandManager):

        soft_and_mobile = [
            'Черній Андрій Олегович',
            'Щербаков Андрій Вікторович',
            'Жук Максим Олегович'
        ]
        game = [
            'Демченко Андрій Сергійович',
            'Заїка Владислав Володимирович',
            'Чащін Дмитро Павлович'
        ]
        try:
            i = agvs[0]
            if i == "program_development":
                for i in soft_and_mobile:
                    self.color.print_command(i)
            elif i == 'game_development':
                for i in game:
                    self.color.print_command(i)
        except IndexError:
            errorText = self.commandConfig.get_text("invalidArgument")
            self.color.print_error(errorText)
            self.write_help()
