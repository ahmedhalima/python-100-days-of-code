import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get('SMTP_HOST', "")
port = int(os.environ.get('SMTP_PORT', 25))
username = os.environ.get('SMTP_USERNAME', "")
password = os.environ.get('SMTP_PASSWORD', "")
from_address = os.environ.get('SMTP_FROM', "")

def send_email(to_address, message, subject):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
    msg.set_content(message)

    try:
        connection = smtplib.SMTP(host, port, timeout=10)
        connection.starttls()
        connection.login(user=username, password=password)
        connection.send_message(msg)
        connection.quit()
        # print('email sent')
    except Exception as e:
        print(f'Failed to send email: {e}')