# twitter authorization
# place your keys in a keys.py file as variables with names like your_consumer_key etc

import keys 
import tweepy

# Authenticate
def get_twitter_auth():
	
	consumer_key = keys.your_consumer_key
	consumer_secret = keys.your_consumer_secret
	access_token = keys.your_access_token
	access_token_secret = keys.your_access_token_secret

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return auth

def get_twitter_client():
	auth = get_twitter_auth()
	api = tweepy.API(auth)
	return api
