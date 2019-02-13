from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(subject,template,to):
    sender_email= 'kelvinadeu25@gmail.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt")
    email.html = render_template(template + ".html")
    mail.send(email)
