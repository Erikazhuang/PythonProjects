import pytest
import user 


def test_get_id_by_name_correct():
    uid = user.get_id_by_name('luna')
    assert uid ==1


def test_get_id_by_name_missing():
    uid = user.get_id_by_name('nobody')
    assert uid ==0


import smtplib, ssl
from web.config import Config

def test_send_email():
    port = 465
    smtp_server = Config.MAIL_SERVER
    sender_email='erikazhuang@gmail.com'
    receiver_email='erikazhuang@gmail.com'
    password = '7791350184'
    message = """
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email, message)