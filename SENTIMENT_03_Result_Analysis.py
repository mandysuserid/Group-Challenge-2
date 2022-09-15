import pandas as pd
import datetime as dt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sql


def ResultAnalasys():
    SQL = 'EXEC [SENTIMENT].sp_GET_MediaDetails'
    media_df = sql.RunSQL_SELECT(SQL,None)
    #print(media_df)
    # Iterating over the tweets in the dataframe
    for idx, row in media_df.iterrows():
        MediaDetailsID = row.MediaDetailsID
        #news_list.append(row.Summary)
        analyzer = SentimentIntensityAnalyzer().polarity_scores(row.Summary)
        neg = analyzer['neg']
        neu = analyzer['neu']
        pos = analyzer['pos']
        comp = analyzer['compound']
        
        print(neg,neu,pos,comp)

        SQL = 'EXEC SENTIMENT.sp_INSERT_SentimentScore {},{},{},{},{}'.format(MediaDetailsID,neg,neu,pos,comp)
        sql.RunSQL_EXEC(SQL)
