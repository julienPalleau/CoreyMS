import smtplib
from email.message import EmailMessage

email_content = '''Dear Sir/Madam,

I am sending you an e-mail with Python. I hope you like it.

Kind regards,
David
'''

email = EmailMessage()
email['Subject'] = 'Test email'
email['From'] = 'dcorvaisier8@gmail.com'
email['To'] = 'dcorvaisier8@gmail.com'

email.set_content(email_content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('dcorvaisier8@gmail.com', 'supuration')

smtp_connector.send_message(email)
smtp_connector.quit()
