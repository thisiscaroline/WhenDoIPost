# When Do I Post? - Fetches tweet post times and graphs them

import math
import matplotlib.pyplot as plt
import pytz
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
	
	print('\n')
	
	# Fetch tweets
	tweets = api.user_timeline(screen_name = username, count = tweetCount)
	tweetList = []
	
	# Create a graph
	plt.axis([1,7,0,12])
	plt.xlabel('Days')
	plt.ylabel('Hours')
	
	# Add tweet timestamps to list; time is in UTC
	for tweet in tweets:
	
		try:
			if (tweet.text[:2] == "RT"):
				print("\x1b[1;32mRetweet \x1b[0m", end=" ")
			print(tweet.text, end="\n")
		except:
			# TODO: Error checking, replace emoji?
			pass
			
		tweetList.append(tweet.created_at)
		print("\t"+str(tweet.created_at)+"\n")
	
	# Create data points out of each timestamp
	# x: Day of the week; y: Time they tweeted
	for i in range(0, len(tweetList)):
		
		tz = pytz.timezone('America/New_York')
		timestamp = tz.localize(tweetList[i])
		# print(str(timestamp))
		
		#print(tweetList[i], end=": ")
		x = form_x(str(tweetList[i].ctime()))
		y = form_y(tweetList[i])
		#print(str(x)+", "+str(y))
	
	# plt.show()
	
# Decides and returns an x-coordinate
def form_x(tweet):
	
	# print(tweet[:3], end=": ")
	return {
		'Sun': 1,
		'Mon': 2,
		'Tue': 3,
		'Wed': 4,
		'Thu': 5,
		'Fri': 6,
		'Sat': 7,
	}[tweet[:3]]

# Converts 24h time to 12h, minutes to increments
def form_y(tweet):
	
	# print(str(tweet.hour)+":"+str(tweet.minute))
	hour, minutes = 0, 0
	
	# Mod the hour, if necessary
	if (tweet.hour == 0):		# Midnight
		hour = 0
	elif (tweet.hour < 12):		# AM hours
		hour = tweet.hour
	elif (tweet.hour == 12):	# Noon
		hour = 12
	elif (tweet.hour > 12):		# PM hours
		hour = (tweet.hour % 12)
	
	# Minutes as a fraction of the hour
	minutes = round(tweet.minute/60,2)
	
	return (hour+minutes)
			
if __name__ == '__main__':
	main()
