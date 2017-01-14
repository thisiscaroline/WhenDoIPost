# When Do I Post? - Fetches tweet post times and graphs them

import tweepy
from tweepy import OAuthHandler
import sys

consumerKey = 'YOUR_CONSUMER_KEY'
consumerSecret = 'YOUR_CONSUMER_SECRET'
accessToken = 'YOUR_ACCESS_TOKEN'
accessSecret = 'YOUR_ACCESS_SECRET'

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth)

def main():

	# Pick a username
	username = input("Enter a username here: \n>> ")
	
	# Fetch tweets
	tweets = api.user_timeline(screen_name = username, count=10)
	
	for tweet in tweets:
		print(tweet.created_at)
		
if __name__ == '__main__':
	main()
