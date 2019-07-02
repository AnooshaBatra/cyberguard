from tester import *
from getTweets import get_tweets
import sys
#username="mavelloussamad"
username=sys.argv[1]
n=list()
n.append(get_tweets(username))
print("Tweet: ",n[0])
#n=["you are good"]
preprocessed=preprocess(n)
tokenized=tokenize(preprocessed)
stopwords_removed=removeStopWords(tokenized)
lemmatized=getlemmatized(stopwords_removed)
vectorized=getVector(lemmatized)

prednew= model.predict(vectorized)
if prednew==1:
    print("Status: Bullying")
elif prednew==0:
    print("Status: Not Bullying")

