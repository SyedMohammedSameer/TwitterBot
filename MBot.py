import tweepy
import time

consumer_key = 'nYO6VUfEP9OskO8la78Ch0CJ3'
consumer_secret = 'wA3Y0XuKxC8nsB4prdPtnQZ2JvdqfDH6LG1nedVnbBa5HXUNVC'

key = '1415979618092212224-gL1zExP9uKSXkAZNEvCKLI9pFv71ev'
secret ='bsNP4nW5TF9SKPfxtcYNFC6CpSX21qWGPYzqCD9fDWMME'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write =open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#ultimatebot' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Auto Reply , like , retweet work",tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)