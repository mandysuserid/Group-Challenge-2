import pandas as pd
import datetime as dt
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import sql
import time

def PullGoogleArticles():
    start = dt.date.today()
    start = start.strftime('%m-%d-%Y')
    end = dt.date.today() - dt.timedelta(days = 10)
    end = end.strftime('%m-%d-%Y')
    print(start,end)

    nltk.download('punkt')
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 10

    KeyWordsdf = sql.RunSQL_SELECT('EXEC [SENTIMENT].[sp_GET_TickerKeywords]',None)

    for idx, row in KeyWordsdf.iterrows():
        Ticker = row.Ticker
        TickerID = row.TickerID
        print(f'Searching for and analyzing {Ticker}, Please be patient, it might take a while...')

        #Extract News with Google News
        googlenews = GoogleNews(lang='en', start=end,end=start)
        googlenews.search(Ticker)

        for i in range(1,10):
            print("Fetching page {}".format(i))
            googlenews.getpage(i)
            result=googlenews.result()
            df=pd.DataFrame(result)

        #df = df[df['datetime']>=(dt.datetime.now()-dt.timedelta(hours=24))].drop_duplicates() #hours = 6,12, 24
        #print(df.head())

        try:
            for i in df.index:
                
                Link = df['link'][i]
                article = Article(df['link'][i],config=config) #providing the link
                try:
                    article.download() #downloading the article 
                    article.parse() #parsing the article
                    article.nlp() #performing natural language processing (nlp)
                except:
                    pass 

                #storing results in our empty dictionary
                PublishDateTime=df['datetime'][i].replace(tzinfo=None) 
                MediaType='Web'
                MediaName = str(df['media'][i])
                Title = str(article.title)
                AtricleText = str(article.text)
                ArticleSummary=str(article.summary)
                Keywords=str(article.keywords)
                print("Parcing article for {}".format(MediaName))

                SQL = "EXEC SENTIMENT.[sp_INSERT_MediaDetails] {},'{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}'".format(TickerID,PublishDateTime,MediaType,MediaName,None,Title.replace("'",""),AtricleText.replace("'",""),ArticleSummary.replace("'",""),Keywords.replace("'",""),Link)
                sql.RunSQL_EXEC(SQL)

        except Exception as e:
            #exception handling
            print("exception occurred:" + str(e))
            print('Looks like, there is some error in retrieving the data, Please try again or try with a different ticker.' )

        #Lets wait 
        time.sleep(900)

PullGoogleArticles()
