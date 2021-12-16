from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from os import environ
from dotenv import load_dotenv

load_dotenv()


def send_newsletter(subject, lead_message, recipients, names):
    email = MIMEMultipart()

    password = environ.get("EMAIL_PASSWORD")
    email['From'] = environ.get("EMAIL_FROM")

    recipients_list = recipients
    names_list = names

    email['To'] = ", ".join(recipients_list)
    email['Subject'] = subject

    message_body = lead_message

    # to do -> como enviar com os nomes dos leads
    message = f"Hello dev! \n \n {message_body} \n \n Cheers! \n ComunicaDev Team"

    email.attach(MIMEText(message, 'plain'))
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(email['From'], password)
        server.sendmail(email['From'], recipients_list, email.as_string())
        server.quit()