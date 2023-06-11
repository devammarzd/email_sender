import smtplib
from email.message import EmailMessage
#https://docs.python.org/3/library/email.message.html
from string import Template
from pathlib import Path

htmlTemplate = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Python Experto'
email['to'] = '<reciepent email address>'
email['subject'] = 'You won 1,000 US Dollars!!'

# email.set_content("I am a Python Master!")
email.set_content(htmlTemplate.substitute({'name': "John"}),'html')
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<sender email address>', '<password>')
    #https://myaccount.google.com/apppasswords for the password from less secure device
    smtp.send_message(email)
    print("Email Sent Successfully!")




