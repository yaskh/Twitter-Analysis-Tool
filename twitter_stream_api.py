import tweepy
import csv
import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys 
from tweepy import API

####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

tweets = []
class StdOutListener(StreamListener):

    def __init__(self, output_file=sys.stdout):
        super(StreamListener,self).__init__()
        self.output_file = output_file
    def on_data(self, data):
        #if data['lang'] == 'en':
        #tweets.append(data)
        with open('tweetfile.json', 'a') as f: 
            f.write(data)
            print(data)
        #writer = csv.writer(f)
        #writer.writerow([data.text])
        	
    def on_error(self, status):
    	print (status)
if __name__ == '__main__':
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = API(auth, wait_on_rate_limit=True,
           wait_on_rate_limit_notify=True)
	output = open("streamdata.json",'w')
	l = StdOutListener(output_file=output)		    	
	try:	
		stream = Stream(api.auth, l,output_file = output)

		    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
		stream.filter(track=['trump','imran khan'],languages=['en'])
	except KeyboardInterrupt:
		print("stopped")
	finally:
		print("Done")
		stream.disconnect()
		output.close()
