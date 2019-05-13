import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import command.color

class Email:

    def __init__(self, commandManager):
        self.color = command.color.Color()
        self.email = commandManager.commandConfig.get_config()['Email']['email']
        self.password = commandManager.commandConfig.get_config()['Email']['password']


    def send(self, to, message, subject=''):
        if self.email == '' or self.password == '' :
            print("Email Error: Email or password not found. To set email - in config.json find \"Email\" and type email and password.")
        else:
            try:
                msg = MIMEMultipart()
                msg['From'] = self.email
                msg['To'] = to
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(self.email, self.password)
                text = msg.as_string()
                server.sendmail(self.email, to, text)
                server.quit()
            except Exception as e:
                self.color.print_error("Failed to send mail")
