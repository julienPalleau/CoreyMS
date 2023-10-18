import requests

MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandbox8fc97ff7f4ec44d2b8819d0a8498762d.mailgun.org'
MAILGUN_API_KEY = 'c11ef55fbac7c8d724adba412d1f68a3-2bf328a5-893a3cb6'

FROM_NAME = 'David'
FROM_EMAIL = 'dcorvaisier8@gmail.com'

TO_EMAILS = ['dcorvaisier8@gmail.com']
SUBJECT = 'Test e-mail'
CONTENT = 'Hello, this is a test e-mail'

requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),  # This is Basic Auth
    data={
        'from': f'FROM_EMAIL <{FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    })
