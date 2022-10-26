import requests


class Mailgun:
    MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandbox8fc97ff7f4ec44d2b8819d0a8498762d.mailgun.org'
    MAILGUN_API_KEY = 'c11ef55fbac7c8d724adba412d1f68a3-2bf328a5-893a3cb6'

    FROM_NAME = 'David'
    FROM_EMAIL = 'dcorvaisier8@gmail.com'

    @classmethod
    def send_email(cls, to_emails, subject, content):
        def send_simple_message():
            return requests.post(
                "https://api.mailgun.net/v3/sandbox8fc97ff7f4ec44d2b8819d0a8498762d/messages",
                auth=("api", cls.MAILGUN_API_KEY),
                data={"from": f'{cls.FROM_NAME} <{cls.FROM_EMAIL}>',
                      "to": to_emails,
                      "subject": subject,
                      "text": content})


