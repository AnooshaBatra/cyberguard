from flask import Flask, request, jsonify
import traceback
import pickle
import pandas as pd
import numpy as np

import re, string, nltk
from nltk.corpus import stopwords
import re, string, nltk
from nltk.corpus import stopwords
import pickle
from getTweets import get_tweets
import sys
from tester import *

app = Flask(__name__)



@app.route('/predict/<string:data>', methods=['GET', 'POST'])
def predict(data):
	try:
		
		n=list()
		
		n.append((get_tweets(data)))
		print(n)
		
		preprocessed=preprocess(n)
		tokenized=tokenize(preprocessed)
		stopwords_removed=removeStopWords(tokenized)
		lemmatized=getlemmatized(stopwords_removed)
		vectorized=getVector(lemmatized)
		prednew= model.predict(vectorized)
		if prednew==1:
			return "Status: Bullying"
		elif prednew==0:
			return "Status: Not Bullying"
		
	except:
		return jsonify({'trace': traceback.format_exc()})
	
 @app.route("/")
def index():
    return "Welcome to machine learning model APIs! Cyberguard"

if __name__ == '__main__':
	try:
		port = int(sys.argv[1])
# This is for a command-line argument
	except:
		port = 12345
	
	app.run(debug=True,port=port)
