import smtplib
from email.message import EmailMessage
u = input('enter your email: ')
p = input('enter your password: ')
ema= input('enter the email you want to send the email to: ')
email = EmailMessage()
name= input('enter your name: ')
email['from'] = name
email['to']= ema
email['subject'] = 'Test Email'

email.set_content('hello world,this is a test email')

with smtplib.SMTP(host= 'smtp.gmail.com',port=535) as smtp: #host and port for gmail can be found on google
    smtp.ehlo() #identifies ourselves with the mail server that we are using
    smtp.starttls()#encrytion method kind of
    smtp.login(f'{u}',f'{p}') #enter your email and password
    smtp.send_message(email)
    print('all good boss!') #if this prints then the email has been sent
    
