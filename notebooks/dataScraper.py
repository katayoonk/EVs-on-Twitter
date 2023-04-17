import sys
import pandas as pd
import datetime 
import snscrape.modules.twitter as sntwitter
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# maximum number of tweets to scrape
filename = ""

def search_query(text, lang, since, until):
    global filename
    query = text

    if lang != '':
        query += f" lang:{lang}"
    if until == '':
        until = datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d')
    query += f" until:{until}"

    if since == '': 
        since = datetime.datetime.strftime(datetime.datetime.strptime(until, '%Y-%m-%d') -  
                                           datetime.timedelta(days=7), '%Y-%m-%d') 
    query += f" since:{since}" 


    filename = f"{since}_{until}_{text}.csv" 

    print(filename) 

    return query

# A function to scrape tweets containing desire word(s) in a span of time and retun a datafram of the tweets
def df_creator(text, lang, until, since):
    # Setting variables to be used below
    query = search_query(text, lang, since, until)
    # Creating list to append tweet data to
    tweets_list = []
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        if i%1000 == 0:
            print(f"Scraped {i} tweet for {query}.\nLast tweet is {tweet}!\n")
    # Creating a dataframe from the tweets list above
    df_temp = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    return df_temp

for i in range(len(sys.argv)):
    print(sys.argv[i])

TEXT = 'Tesla'
LANG = 'en'
UNTIL = '2023-04-10' #datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d')
SINCE = '2020-01-01' #datetime.datetime.strftime(datetime.datetime.strptime(UNTIL, '%Y-%m-%d') - datetime.timedelta(days=7), '%Y-%m-%d') 

if len(sys.argv) >= 2:
    TEXT = sys.argv[1]
if len(sys.argv) >= 3:
    LANG = sys.argv[2]
if len(sys.argv) >= 4:
    UNTIL = sys.argv[3]
if len(sys.argv) >= 5:
    SINCE = sys.argv[4]
df = df_creator(text=TEXT, lang=LANG, until=UNTIL, since=SINCE)
# df = df_creator(text='Model 3 OR Model3 OR Model Y OR Model X', lang='en', until='2023-04-10', since='2022-01-01')


df.to_csv(f"{filename}",index=False)