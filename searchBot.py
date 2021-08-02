import tweepy
import time

consumer_key = 'nYO6VUfEP9OskO8la78Ch0CJ3'
consumer_secret = 'wA3Y0XuKxC8nsB4prdPtnQZ2JvdqfDH6LG1nedVnbBa5HXUNVC'

key = '1415979618092212224-gL1zExP9uKSXkAZNEvCKLI9pFv71ev'
secret ='bsNP4nW5TF9SKPfxtcYNFC6CpSX21qWGPYzqCD9fDWMME'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = "#IndvsSl"
tweetNumber = 5

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(3)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)    

searchBot()