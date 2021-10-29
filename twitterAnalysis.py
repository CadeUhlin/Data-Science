import tweepy
from textblob import TextBlob

consumer_key = 'wjtPYPWfDFodvxEHOYToUseVB'
consumer_secret = 'NYsRy3WtQD7o28xOoQJg078bXQ1R6NtEbDWCgD6OQ6IRg678Hh'

access_token = '1720532642-ySuJz3V8JWt5S24u8qgDB1GLGaGMhHfCiVoWhYx'
access_token_secret = 'gosTwiTmd7YdgIhbfjxFyw0vdxXjCaqHL7jPHA7IZBEr2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print('Please enter a topic to search')
topic = input()

public_tweet = api.search(topic)

for tweet in public_tweet:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)