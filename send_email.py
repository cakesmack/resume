import smtplib, ssl
import credentials

user = credentials.username
mypass = credentials.password

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = user
    password = mypass

    receiver = user

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver, message )