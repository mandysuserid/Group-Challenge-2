import schedule, time
from datetime import datetime
import SENTIMENT_02_1_RedditScraper
import os


def PullReddit():
    SENTIMENT_02_1_RedditScraper.RunRedditScrape()

schedule.every(120).seconds.do(PullReddit)
#schedule.every(30).seconds.do()

while True:
    os.system('cls')
    schedule.run_pending()
    current_datetime = datetime.now()
    print(current_datetime)
    time.sleep(60)