import smtplib

def sendSmtpEmail():
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls() #enable security
    sender_address = 'erikazhuang@gmail.com'
    passcode = 'xxxx'
    server.login(sender_address, passcode)
    server.sendmail(sender_address,'erikazhuang@gmail.com','test message email')
    server.quit()