import tweepy
from textblob import TextBlob
from twitter_client import get_twitter_client

api = get_twitter_client()

	
# Retrieve Tweets
public_tweets = api.search('#magicleap')
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 



