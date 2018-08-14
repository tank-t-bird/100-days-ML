import json
import tweepy
from twitter_client import get_twitter_client

api = get_twitter_client()

	
# Retrieve Tweets direct print to terminal
#for status in tweepy.Cursor(api.home_timeline).items(10):
#	print(status.text)

# Retrieve tweets to json

with open('home_timeline.jsonl', 'w') as f:
	for page in tweepy.Cursor(api.home_timeline, count=10).pages(1):
		for status in page:
			f.write(json.dumps(status._json)+"\n")