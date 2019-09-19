import sys
sys.setrecursionlimit(5000)
import simplejson as json
from elasticsearch import Elasticsearch
import pandas as pd 
from elasticsearch.helpers import bulk
es = Elasticsearch()

mappings = {  
   "settings":{
	"index" : {
        	"number_of_shards" : 5, 
	        "number_of_replicas" : 1 
    	},
   "index.mapping.total_fields.limit" : 10000, 
   }
  }
    
es.indices.create(index="trump", body=mappings, ignore=400)
#data = pd.read_json("tweetfile.json")
tweets = []

for line in open('tweetfile.json', 'r'):
    if line.strip() != "":
        message = json.loads(line)
        id = message["id"]
        del(message["id"])
        tweet = {
                '_id': id,
                '_source':message,
                '_index' : 'trump'
                }
        tweets.append(tweet)
        
    if len(tweets) == 1000:
        bulk(es,tweets)
        tweets.clear()
bulk(es,tweets)
tweets.clear()
