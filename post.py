# When Do I Post? - Fetches tweet post times and graphs them

import datetime
import matplotlib.pyplot as plt
import sys
import tweepy

from tweepy import OAuthHandler

consumerKey = 'YOUR_CONSUMER_KEY'
consumerSecret = 'YOUR_CONSUMER_SECRET'
accessToken = 'YOUR_ACCESS_TOKEN'
accessSecret = 'YOUR_ACCESS_SECRET'

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)

def main():

	try:		# Check for a help flag
		if sys.argv[1] == "-h":
			print("To use: py post.py [username] [number of tweets]")
			sys.exit()
	except:
		pass	# Do nothing

	# Get username, number of tweets
	if len(sys.argv) == 3:
		username = sys.argv[1]
		tweetCount = sys.argv[2]
	else:
		username = input("Enter a username:\n>> ")
		tweetCount = input("Enter the number of tweets you'd like to analyze:\n>> ")
	
	# Fetch tweets
	tweets = api.user_timeline(screen_name = username, count = tweetCount)
	tweetList = []
	
	print('\n')
	
	# Print tweet times
	for tweet in tweets:
		print("\x1b[1;32m%s\x1b[0m" % str(tweet.created_at))
		tweetList.append(tweet.created_at)
	
	print('\n')
	
	for i in range(0, len(tweetList)):
		print(tweetList[i])
	
	
	# Create a graph
	plt.axis([1,7,0,12])
	plt.xlabel('Days')
	plt.ylabel('Hours')
	plt.show()
			
if __name__ == '__main__':
	main()
