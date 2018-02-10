import json
import ast
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

keys = []
with open('tokens.txt') as f:
    keys = (f.readlines())

ACCESS_TOKEN = keys[0].split("=")[1].strip()
ACCESS_SECRET = keys[1].split("=")[1].strip()
CONSUMER_KEY = keys[2].split("=")[1].strip()
CONSUMER_SECRET = keys[3].split("=")[1].strip()

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)


d = twitter.search.tweets(q='Flint lead poisoning -filter:retweets', lang='en', count=10)

with open('test.json', 'w') as fout:
    json.dump(d, fout)

#parse to CSV
#user_handle, date, text
csv_output = []

for tweets in d['statuses']:
    test = tweets['user']['screen_name'] + ',' + tweets['created_at'] + ',' + tweets['text'].replace('\n', '')
    #link = []
    #for links in tweets['retweeted_status']['entities']['urls']:
    #    link.append(links['url'])

    csv_output.append(test)# + str(link))

with open('data.csv', 'w') as fout:
    for line in csv_output:
        fout.write(line.encode('utf-8').strip() + '\n')