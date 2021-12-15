from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from os import environ
from dotenv import load_dotenv
from .verify_user_email import generate_shorten_link

load_dotenv()


def send_reset_password_code(user_name, user_email, code):
    email = MIMEMultipart()

    password = environ.get("EMAIL_PASSWORD")
    email['From'] = environ.get("EMAIL_FROM")

    email['To'] = user_email
    email['Subject'] = 'ComunicaDev - Reset password request'

    message = f' Hello {user_name}! \n \n Your code to reset your password: {code} \n \n Cheers! \n ComunicaDev Team'

    email.attach(MIMEText(message, 'plain'))
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(email['From'], password)
        server.sendmail(email['From'], email['To'], email.as_string())
        server.quit()