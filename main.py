import nltk
import csv
import re
import nltk
nltk.download('stopwords')
from nltk.tokenize import TreebankWordTokenizer
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
stopword = stopwords.words("english")
from nltk.stem import *
stemmer = PorterStemmer()
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import collections

datafile = open('tweets.csv', 'r')
myreader = csv.reader(datafile)
tweets=[]
for row in myreader:
    row[0]=re.sub("@", "", row[0])
    row[0]=row[0].lower()
    row[0]=re.sub('[^A-Za-z]+', ' ', row[0])
    for stp in stopword:
        row[0]=row[0].replace(' '+stp+' '," ")
    row[0]=re.sub(" [a-zA-Z]{3} | [a-zA-Z]{3}$|^[a-zA-Z]{3} ", " ", row[0])
    row[0]=re.sub(" [a-zA-Z]{2} | [a-zA-Z]{2}$|^[a-zA-Z]{2} ", " ", row[0])
    row[0]=re.sub(" [a-zA-Z] | [a-zA-Z]$|^[a-zA-Z] ", " ", row[0])

    tokens=TreebankWordTokenizer().tokenize(row[0])
    for t in tokens:
        stem=stemmer.stem(t)
#        print(stem)

    twlist=[]
    twlist.append(row[0])
    tweets.append(twlist)

with open('outputdata.csv', 'w') as outfile:
    mywriter = csv.writer(outfile)
    # manually add header

    mywriter.writerow(['tweet'])
    for d in tweets:

        mywriter.writerow(d)

df = pd.read_csv(r"outputdata.csv", encoding ="latin-1")
 
comment_words = ''
stopwords = set(STOPWORDS)
 
# iterate through the csv file
for val in df.tweet:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
 
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
 
# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()

datafile = open('tweets.csv', 'r')
myreader = csv.reader(datafile)
hashtags=[]
for row in myreader:
    tags=re.findall("#[a-zA-Z]+", row[0])
    for t in tags:
        hashtags.append(t)
w = collections.Counter(hashtags)
plt.bar(w.keys(), w.values())
plt.show()