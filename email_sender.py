import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

host = 'smtp.gmail.com'
port = 465

my_email_username = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
subject = '🚀 New Message from Yoni Leventhal - Thank you for reaching out!'


def send_email(users_email_username, username):
    body = f"""Hi {username},
    Thank you for getting in touch! I appreciate your interest in my projects.
    I’ll do my best to get back to you as soon as possible.

    In the meantime, feel free to check out more of my projects on the website and share any thoughts or questions you may have.

    Thanks again, and have a wonderful day!
    Yoni Leventhal
    """

    msg = MIMEMultipart()
    msg['From'] = my_email_username
    msg['To'] = users_email_username
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the Gmail SMTP server and send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(my_email_username, password)
        server.sendmail(my_email_username, users_email_username, msg.as_string())
        print('Successfully sent email')