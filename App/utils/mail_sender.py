import yagmail


class MailSender:
    def __init__(self, address: str, password: str) -> None:
        self.yag = yagmail.SMTP(user=address, password=password)

    def send_mail(self, rec: str, subject: str, message: str) -> None:
        self.yag.send(to=rec, subject=subject, contents=message)
