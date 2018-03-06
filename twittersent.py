import tweepy
from textblob import TextBlob

consumer_key = 	'Xy8fde3HqQk7DWpgtXboFfmri'
consumer_secret = 'wsPlJIih0VJUAWYYJHbD0PmtZo7WUzZtb1yw3sSwJdGs7OTrW8'

acess_token = '943914534-JuJq9elxb9y2VjVyEI979XIyiyuB6hNscgETQB1k'
acesss_token_secret= 'adOOwJJy6uObPFWLjuZfJ41ZENrDra0FGz4N6Iu4dtsRV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acesss_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("memes", count=100)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)