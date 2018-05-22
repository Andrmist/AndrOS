import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:

    def __init__(self, commandManager):
        self.email = commandManager.commandConfig.get_config()['Email']['email']
        self.password = commandManager.commandConfig.get_config()['Email']['password']


    def send(self, to, message, subject=''):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, to, text)
        server.quit()