#loding pickle
import pickle
with open('cb.pickle', 'rb') as tr:  
    model = pickle.load(tr)
print("model loaded")

import re, string, nltk
from nltk.corpus import stopwords
def preprocess(s):
    #lower
    s=s[0].lower()
    #remove numbers
    s=re.sub(r'\d+','',s)
    #remove symbols
    s=s.translate(str.maketrans('','',string.punctuation))
    #removeing single and double characters
    s=re.sub(r'\b[a-zA-Z]\b',' ',s)
    s=re.sub(r'\b[a-zA-Z][a-zA-Z]\b',' ',s)
    #remove whitespaces
    s=re.sub(r'\s+', ' ', s, flags=re.I)
    #Convert www.* or https?://* to URL
    s = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',s)
    #Convert @username to AT_USER
    s = re.sub('@[^\s]+','AT_USER',s)
    #Replace #word with word
    s = re.sub(r'#([^\s]+)', r'\1', s)
    return s
    
def tokenize(s):
    tokenizer = nltk.tokenize.TreebankWordTokenizer()
    return tokenizer.tokenize(s)    
    
def removeStopWords(s):
    stop_words = set(stopwords.words('english'))  #nltk file
    with open("stopwords.txt") as file:
        for line in file:
            stop_words1=line.split(",")  #opensource
    tmp=[]
    for i in s:
        if (not i in stop_words) and (not i in stop_words1):
            tmp.append(i)
    return tmp

def getlemmatized(s):
    lemmatizer= nltk.stem.WordNetLemmatizer()
    a=[]
    a.append(" ".join(lemmatizer.lemmatize(word,'n') for word in s))
    s=a[0].split()
    a=[]
    a.append(" ".join(lemmatizer.lemmatize(word,'v') for word in s))    
    return a

import pickle
with open('vectorizer.pickle', 'rb') as picklefile:  
    vectorizer = pickle.load(picklefile)
print("vectorizer loaded")
            
def getVector(s):
    from sklearn.feature_extraction.text import TfidfVectorizer  
    #tfidfconverter = TfidfVectorizer(max_features=15000, min_df=3, max_df=0.7)
    corpus=s
    x = vectorizer.transform(corpus)
    #feature_names=tfidfconverter.get_feature_names()
    feature_vectors=x.toarray()
    return x #feature_vectors
