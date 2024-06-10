import yagmail


class MailSender:
    def __init__(self, address, password):
        self.yag = yagmail.SMTP(user=address, password=password)


    def send_mail (self, rec, subject, message):
        self.yag.send(to=rec, subject=subject, contents=message)
