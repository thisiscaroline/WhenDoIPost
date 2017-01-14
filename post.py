# When Do I Post? - Fetches tweet post times and graphs them

import datetime
# import matplotlib.pyplot as plt
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
	s = Stack()
	
	for tweet in tweets:
		tweetDate = tweet.created_at	# tweet.created_at == datetime.datetime object
		s.push(tweetDate)
		
	print("\n\n")
	
	for i in range(0, s.size()):
		print(str(i+1)+": "+str(s.pop().ctime()))
		


# Simple stack implementation
class Stack:
		def __init__(self):
			self.container = []
		def isEmpty(self):
			return self.size == 0
		def push(self, item):
			self.container.append(item)
		def pop(self):
			return self.container.pop()
		def peek(self):
			print((self.container[len(self.container)-1]).ctime())
		def size(self):	
			return len(self.container)
			
if __name__ == '__main__':
	main()
