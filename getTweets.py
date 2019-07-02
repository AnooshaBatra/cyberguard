
import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "ydHhvBAHcY71IcLs38umdQpfv" 
consumer_secret = "mGDWflKeMJ8LYlzAkMBZe86tp63UCvfV0suzjyNUP55TunhWtt"
access_key = "1417945135-SA2sGseUmOjASFH6g1BY5dFPj1IGdxXfs4B7s1M"
access_secret = "U3m0w2Nog8BCWOG2ttHtlRQiHO0hrmcU23oBzeUEgDVha"

  
# Function to extract tweets 
def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        return tmp[0]
  
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("mavelloussamad")
    
