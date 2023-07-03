import resend
import os
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(sender, to, subject, html):
    r = resend.Emails.send({"from": sender, "to": to, "subject": subject, "html": html})
    return r
