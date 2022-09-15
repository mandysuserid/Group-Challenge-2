CLIENT_ID =  'xX38sZjeyly8d5LcYRRB0g' 
SECRET_KEY = '9I7OY4ciafNYDywCeiDt4g3oXOW-bw'

from logging import exception
import requests
import pandas as pd
import sql
from datetime import datetime
import time
import SENTIMENT_03_Result_Analysis

def RunRedditScrape():
    print("Pulling Reddit Data")
    print("Authenticating...")
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    data = {
        'grant_type': 'password',
        'username': 'jverhei79',
        'password': '1mustang00'
    }

    KeyWordsdf = sql.RunSQL_SELECT('EXEC [SENTIMENT].[sp_GET_TickerKeywords]',None)
    #print(df)
    
    try:
        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

        TOKEN = res.json()['access_token']
        headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

        response = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

        Subreddits = [
            'r/Investing'
            ,'r/Stocks'
            ,'r/Economics'
            ,'r/StockMarket'
            ,'r/Economy'
            ,'r/GlobalMarkets'
            ,'r/WallStreetBets'
            ,'r/Options'
            ,'r/Finance'
            ,'r/Dividends'
            ,'r/Cryptocurrency'
            ,'r/SecurityAnalysis'
            ,'r/AlgoTrading'
            ,'r/DayTrading'
            ,'r/PennyStocks'
            ,'r/ValueInvesting'
            ,'r/RealDayTrading'
        ]

        RedditURL = 'https://oauth.reddit.com/'
        hot = '/hot'
        new = '/new'

        print("Pulling data...")
        for sub in Subreddits:
            URL = RedditURL + sub + new
        
            res = requests.get(URL, headers=headers)
            #df = pd.DataFrame()
            #print(res.json()['data'])
            
            for post in res.json()['data']['children']:
                subreddit =  post['data']['subreddit']
                subredditID =  post['data']['subreddit_id']
                PostID =  post['data']['id']
                title =  post['data']['title'].replace("'","''")
                selftext =  post['data']['selftext'].replace("'","''")
                #upvote_ratio =  post['data']['upvote_ratio']
                #ups =  post['data']['ups']
                #downs =  post['data']['downs']
                #score =  post['data']['score']
                createdTimeStamp =  post['data']['created']
                createdDateTime = datetime.fromtimestamp(createdTimeStamp)

                for idx, row in KeyWordsdf.iterrows():
                    if row.Ticker in title or row.Ticker in selftext or row.Keyword1 in title or row.Keyword1 in selftext or row.Keyword2 in title or row.Keyword2 in selftext:
                         sql.RunSQL_EXEC("EXEC SENTIMENT.[sp_INSERT_MediaDetails] {},'{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}'".format(row.TickerID,createdDateTime,'Social','Reddit/' + sub,subredditID+','+PostID,title,selftext,None,None,None))

            #print(createdDateTime, subreddit, title)
            

    except exception as e:
        print("Error Authenticating: {}".format(e))
        time.sleep(60)

    #Run the analasys
    SENTIMENT_03_Result_Analysis.ResultAnalasys()
    

#RunRedditScrape()