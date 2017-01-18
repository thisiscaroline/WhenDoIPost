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
		tweetCount = int(sys.argv[2])
	else:
		username = input("Enter a username:\n>> ")
		tweetCount = input("Enter the number of tweets you'd like to analyze:\n>> ")
	
	# print('\n')
	
	# Create a graph
	plt.axis([1,7,0,12])
	plt.xlabel('Sunday     Monday     Tuesday     Wednesday     Thursday     Friday     Saturday')
	plt.ylabel('Hours')
	
	# Variables for later use
	count = 1
	clr = 'green'
	tweetList = []
	
	# Fetch tweets, change timezones
	for tweet in tweepy.Cursor(api.user_timeline, id=username).items(tweetCount):
			
		try:
			local_tz = localize_times(tweet.created_at)
			tweetList.append(local_tz)
		except:
			pass # TODO: Error checking, replace emoji?
			
		count+=1
	
	# Create data points out of each timestamp
	# x: Day of the week; y: Time they tweeted
	for i in range(0, len(tweetList)):
			
		x = form_x(str(tweetList[i].ctime()))
		y = form_y(tweetList[i], 'y')
		
		minLabel = "0"+str(tweetList[i].minute) if tweetList[i].minute < 10 else str(tweetList[i].minute)
		timeLabel = str(form_y(tweetList[i], 'n'))+":"+minLabel
		
		# Set AM or PM colors
		if tweetList[i].hour < 12:
			clr = 'r'
			plt.annotate(timeLabel+" AM", xy=(x,y), xytext=(x+0.15,y+0.15))
		else:
			clr = 'b'
			plt.annotate(timeLabel+" PM", xy=(x,y), xytext=(x+0.15,y+0.15))
		
		# Plot the coordinates on the graph
		plt.scatter(x, y, c=clr, s=75, marker='o', edgecolors='black')
	
	plt.show()
		
# Changes timezone from UTC to EST
def localize_times(utcTime):

	local_tz = pytz.timezone('America/New_York')
	local_dt = utcTime.replace(tzinfo=pytz.utc).astimezone(local_tz)
	
	return local_dt
	
# Decides and returns an x-coordinate
def form_x(tweet):
	
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
def form_y(tweet, yn):
	
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
	
	# Plotting vs. aesthetic decision
	if yn == 'y':
		# Plot as a fraction of the hour
		minutes = round(tweet.minute/60,2)
	elif yn == 'n':
		# Print the hour as text
		if hour == 0:
			return 12
		return hour
	
	return (hour+minutes)
			
if __name__ == '__main__':
	main()
