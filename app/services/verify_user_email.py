from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from os import environ
from dotenv import load_dotenv

load_dotenv()

def verify_user_email(user_name, user_email, user_token):
    email = MIMEMultipart()

    password = environ.get("EMAIL_PASSWORD")
    email['From'] = environ.get("EMAIL_FROM")

    email['To'] = user_email
    email['Subject'] = 'ComunicaDev - Verify your email'

    # link = f'https://comunica-dev-api.herokuapp.com/api/users/validate/{user_token}'

    link = f'http://127.0.0.1:5000/api/users/validate/{user_token}'

    message = f"Hello {user_name}! \n \n Please click on the link below to confirm your email: \n \n {link} \n \n Cheers! \n ComunicaDev Team"

    email.attach(MIMEText(message, 'plain'))
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(email['From'], password)
        server.sendmail(email['From'], email['To'], email.as_string())
        server.quit()