import sys
import webbrowser
import tweepy
import os, requests
from datetime import date




consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("SECRET_API_KEY")
access_token =  os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



current_tweets = []



#URL="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2"


def program_args():
    twitter_username = sys.argv[1:]
    if len(twitter_username) < 1:
        raise Exception("twitter user name can not be empty")

    else:
        twitter_username = twitter_username
       
    
    return twitter_username

def user_tweets(username):
    current_day =  date.today()
    print(current_day)
    print(username[0])
    tweets = api.user_timeline(id=username[0], count=10)

    
    users = api.lookup_users(screen_names=username)
#gets the user only if it exists
#here I need to make it be so that it only gets the tweet for the current tweet
#then it will be done
# need to set up array to store the tweets
# need to then work on sending message

    if users is not None:
        for tweet in tweets:
          
            #change to crrent_date later
            #this is just to test if it is working

            #-- todo -- 
            # add the data to a dictionary/array
            #  incorperate twillio/ look at examples

            if(tweet.created_at.date() == date(2020, 8,18)):
                current_tweets.append({'text':tweet.text})
                
                



    else:
        print("user does not exist")

    return current_tweets
   
    
      
    
    
    
    


username = program_args()

tweets = user_tweets(username)
print(tweets)
