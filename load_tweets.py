import tweepy
from textblob import TextBlob

# Gain Twitter access - insert your credentials.
api_key = '____________'
api_key_secret = '_________'
access_token = '__________'
access_token_secret = '______________'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

user = tweepy.API(auth)

def stock_sentiment(quote, num_tweets):
    # Checks if the sentiment for our quote is positive
    tweet_list = user.search(quote, count=num_tweets)
    positive, null = 0, 0

    for tweet in tweet_list:
        blob = TextBlob(tweet.text).sentiment
        if blob.subjectivity == 0:
            null += 1
            next
        if blob.polarity > 0:
            positive += 1
        print(tweet_list)

    if positive > ((num_tweets - null) / 2):
        return True
