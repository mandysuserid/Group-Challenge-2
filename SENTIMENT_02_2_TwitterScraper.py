# https://tradewithpython.com/sentiment-analysis-for-stocks-from-twitter
import datetime as dt
import sql
import snscrape.modules.twitter as sntwitter
import nltk
import SENTIMENT_03_Result_Analysis

noOfTweet = 10000
now = dt.date.today()
now = now.strftime('%Y-%m-%d')
end = dt.date.today() - dt.timedelta(days = 3)
end = end.strftime('%Y-%m-%d')
start = dt.date.today() - dt.timedelta(days = 4)
start = start.strftime('%Y-%m-%d')
#print(now,yesterday,TwoDaysAgo)

nltk.download('vader_lexicon') #required for Sentiment Analysis
#Get user input
KeyWordsdf = sql.RunSQL_SELECT('EXEC [SENTIMENT].[sp_GET_TickerKeywords]',None)

for idx, row in KeyWordsdf.iterrows():
    #if row.Ticker in title or row.Ticker in selftext or row.Keyword1 in title or row.Keyword1 in selftext or row.Keyword2 in title or row.Keyword2 in selftext:
    print("Working on {}".format(row.Ticker))
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(row.Ticker + ' lang:en since:' +  start + ' until:' + end + ' -filter:links -filter:replies').get_items()):
        if i > int(noOfTweet):
            break
        TweetDate = tweet.date.replace(tzinfo=None)
        SQL = "EXEC SENTIMENT.[sp_INSERT_MediaDetails] {},'{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}'".format(row.TickerID,TweetDate,'Social','Twitter',tweet.id,None,tweet.content.replace("'","").replace("'",""),None,None,None)
        #print(SQL)
        print("Sending {} Tweet {} to DB ... {}".format(row.Ticker,i,tweet.id))
        sql.RunSQL_EXEC(SQL)


#Run the analasys
SENTIMENT_03_Result_Analysis.ResultAnalasys()