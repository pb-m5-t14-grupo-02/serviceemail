import common.constraints as const
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dotenv
import os
import smtplib


def messenger(type: str, topic: str, user: dict) -> None:
    dotenv.load_dotenv()
    msg = MIMEMultipart()
    EMAIL_SENDER = os.getenv(const.EMAIL_ADDRESS)
    EMAIL_RECEIVER = user[const.EMAIL]
    msg[const.FROM] = EMAIL_SENDER
    msg[const.SUBJECT] = topic.capitalize()
    msg[const.TO] = EMAIL_RECEIVER
    if type == const.ON_DATE:
        path = "templates/email_expired.html"
    elif type == const.EXPIRED:
        path = "templates/email_on_date.html"
    else:
        raise KeyError(f"It's necessary use just keys [{const.ON_DATE}, {const.EXPIRED}]")
    with open(path, encoding="utf-8") as f:
        html = f.read()
        html = replace_fields(html, **user)
        msg.attach(MIMEText(html, const.HTML))
    with smtplib.SMTP(os.getenv(const.EMAIL_PROVIDER), int(os.getenv(const.EMAIL_PORT))) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_SENDER, os.getenv(const.EMAIL_PASSWORD))
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

def replace_fields(page, username, year, book, image, author, loan_date, return_date, penalty, **kwargs):
    fields = ("$" + field for field in
             (const.USERNAME, const.YEAR, const.BOOK, const.IMAGE,
             const.AUTHOR, const.LOAN_DATE, const.RETURN_DATE, const.PENALTY))
    values = (username, year, book, image, author, loan_date, return_date, penalty)
    for index, field in enumerate(fields):
        page = page.replace(field, str(values[index]))
    return page
