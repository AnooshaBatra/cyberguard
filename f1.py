from flask import Flask
import pickle
import pandas as pd
import numpy as np

import re, string, nltk
from nltk.corpus import stopwords

app = Flask(__name__)
@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


if __name__ == '__main__':
    app.run(debug=True)