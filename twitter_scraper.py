import re
import requests
import json
import tweepy

username = "realDonaldTrump"
consumer_key = "dl0iyg94jZEfe1TZNTd2dpTKY"
consumer_key_secret = "piyxOZZCWQpeS7PK4E68b13gLCbg0kQ7bIIiytLKevWNyX38gp"
access_token = "889234932555448320-hnw1zGISyUC06O15EwIsVqXYnIVdWcB"
access_token_secret = "2qK6MkQkUklzgD5PRZoKFZStvY8bBarplpaOdiBa4PrHY"
iterations = 10


with open("twitter_output.txt", 'w', encoding='utf-8') as output:

    texts = []
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    new_tweets = []
    oldest_tweet = 0

    for i in range(0, iterations):
        if i > 0:
            # print(new_tweets)
            oldest_tweet = new_tweets[0].id - 1
            new_tweets = api.user_timeline(screen_name=username, count=200, max_id=oldest_tweet)

        else:
            new_tweets = api.user_timeline(screen_name=username, count=200)

        # print(new_tweets)

        # IM GONNA DO THIS THE STUPID WAY FOR NOW

        for tweet in new_tweets:
            # print(tweet)
            string = str(tweet)
            newtweet = re.findall(r'text\'\:\s\'(.+)\'\,\s\'truncated\'\:', string, re.IGNORECASE)

            if len(newtweet) > 0:
                isRT = re.search(r'RT\s@', str(newtweet[0]), re.MULTILINE)
                if(isRT is None):
                    # newtweet = re.sub(r'[\[\]]', r'', str(newtweet))
                    newtweet = re.sub(r'\\n', r' ', str(newtweet))
                    newtweet = re.sub(r'\.\s', r'</s>', newtweet)
                    newtweet = re.sub(r'https?\://.+\'', r'', newtweet)
                    texts.append(str(newtweet))

        # print(texts)

        for text in texts:
            output.write(text)
            output.write("\n")

    output.close()