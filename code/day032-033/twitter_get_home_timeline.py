import tweepy
from textblob import TextBlob
from twitter_client import get_twitter_client

api = get_twitter_client()

	
# Retrieve Tweets
for status in tweepy.Cursor(api.home_timeline).items(1):
	print(status.text)
