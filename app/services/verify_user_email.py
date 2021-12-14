from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from os import environ
from dotenv import load_dotenv
import bitly_api


load_dotenv()


def generate_shorten_link(link):
    BITLY_ACCESS_TOKEN = environ.get('BITLY_ACCESS_TOKEN')

    connection = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)

    shorten_url = connection.shorten(link)

    return shorten_url['url']


def verify_user_email(user_name, user_email, user_token):
    email = MIMEMultipart()

    password = environ.get("EMAIL_PASSWORD")
    email['From'] = environ.get("EMAIL_FROM")

    email['To'] = user_email
    email['Subject'] = 'ComunicaDev - Verify your email'

    BASE_URL = environ.get("BASE_URL")

    link = f'{BASE_URL}/users/validate/{user_token}'

    shorten_link = generate_shorten_link(link)

    message = f"Hello {user_name}! \n \n Please click on the link below to confirm your email: \n \n {shorten_link} \n \n Cheers! \n ComunicaDev Team"

    email.attach(MIMEText(message, 'plain'))
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(email['From'], password)
        server.sendmail(email['From'], email['To'], email.as_string())
        server.quit()