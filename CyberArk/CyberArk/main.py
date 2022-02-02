import csv
import tweepy
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# Oauth keys
consumer_key = "FzQhcfBvKlRwlzLPusKrrSY6P"
consumer_secret = "ITDtL5vsBgyC3N6YrT7sjh8t2WNFNwFeNojLlqmQPH1iIlEaaa"
access_token = "1431117962350448643-59wKX0XbMqwFaI9KDetGi0RlFQKU2G"
access_token_secret = "XIm6pu4mgVX6ocrEVv7WIC9cBKLRnpMFJy9vjn3wRKjFG"
# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'Taylor_Nieman'
tweet_id = '1425868138567012352'
replies=[]
for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name, result_type='recent').items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)
            
with open('replies_clean.csv', 'w', encoding="utf-8") as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)