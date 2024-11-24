import smtplib, ssl
import streamlit as st

user = "cmack6189@gmail.com"
mypass = "tqnmfeefbqyryfpa"

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