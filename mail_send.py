import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(email_host, email_port, email_username, email_password, send_to_address, email_body):
    #Login to email server
    s = smtplib.SMTP(host=email_host, port=email_port)
    s.starttls()
    s.login(email_username, email_password)

    msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
    msg['From']=email_username
    msg['To']=send_to_address
    msg['Subject']="Slim Flix Notification Test"

    # add in the message body
    msg.attach(MIMEText(email_body, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    s.quit()
