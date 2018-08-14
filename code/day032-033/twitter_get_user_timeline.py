import sys
import json
import tweepy
from twitter_client import get_twitter_client

api = get_twitter_client()


# Retrieve tweets to csv
user = sys.argv[1]
fname = "user_timeline{}json1".format(user)

with open(fname, 'w') as f:
	for page in tweepy.Cursor(api.user_timeline, screen_name = user, count=10).pages(1):
		for status in page:
			f.write(json.dumps(status._json)+"\n")
