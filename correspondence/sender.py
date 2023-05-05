from common.constraints import (
    FROM,
    TO,
    SUBJECT,
    EXPIRED,
    ON_DATE,
    R_USERNAME,
    R_RETURN_DATE,
    R_LOAN_DATE,
    R_BOOK,
    R_YEAR,
    R_IMAGE,
    R_AUTHOR,
    R_PENALTY
)
from email.mime.multipart import MIMEMultipart
import dotenv
import os

def messenger(type: str, topic: str) -> None:
    msg = MIMEMultipart()
    dotenv.load_dotenv()
    msg[FROM] = os.getenv("EMAIL_ADDRESS")
    msg[SUBJECT] = topic.capitalize()
    if type == ON_DATE:
        path = "../templates/email_expired.html"
    elif type == EXPIRED:
        path = "../templates/email_on_date.html"
    else:
        raise KeyError(f"It's necessary use just keys [{ON_DATE}, {EXPIRED}]")
    with open(path) as f:
        result = f.read()

        print(result)
    # msg[TO] =


def replace_fields(page, name, year, book, img, author, loan_date, return_date, penality):
    fields = (R_USERNAME, R_YEAR, R_BOOK, R_IMAGE, R_AUTHOR, R_LOAN_DATE, R_RETURN_DATE, R_PENALTY)
    values = (name, year, book, img, author, loan_date, return_date, penality)
    for index, field in enumerate(fields):
        page = page.replace(field, values[index])
    return page

