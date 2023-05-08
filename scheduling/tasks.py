import requests
import schedule
import os
import dotenv
import time
import common.constraints as const
from correspondence.sender import messenger

dotenv.load_dotenv()

def job(type: str, topic: str, endpoint: str):
    print("\033[32mRunning " + type)
    response = requests.get(os.getenv(const.BASE_URL) + endpoint)
    users = response.json()
    for user in users:
        messenger(type, topic, user={
            const.USERNAME: user[const.USER][const.USERNAME],
            const.EMAIL: user[const.USER][const.EMAIL],
            const.PENALTY: user[const.PENALTY],
            const.LOAN_DATE: user[const.LOAN_DATE],
            const.RETURN_DATE: user[const.RETURN_DATE],
            const.IMAGE: user[const.BOOK][const.IMAGE],
            const.BOOK: user[const.BOOK][const.NAME],
            const.YEAR: user[const.BOOK][const.YEAR],
            const.AUTHOR: user[const.BOOK][const.AUTHOR][const.NAME]
            })


schedule.every().day.at(
    os.getenv(const.SEND_TIME_LATE)).do(
    lambda: job(const.ON_DATE, "Livros com prazo de devolução próximo", 
    const.WARN))
schedule.every().day.at(
    os.getenv(const.SEND_TIME_WARN)).do(
    lambda: job(const.EXPIRED, "Livros em atraso",
    const.LATE))
while True:
    schedule.run_pending()
    time.sleep(1)
