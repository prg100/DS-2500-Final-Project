
"""
Patricio Reyes Gomez and Bill (Guanbo) Liu
DS 2500 Final Project
"""

import pandas as pd
import wordcloud as wc
import matplotlib.pyplot as plt
from textblob import TextBlob

df = pd.read_csv("reviews.csv", header = 0, names=["review",'type', "playtime", "upvotes", "funny votes", 'weighted vote score', 'games owned', 'num of other reviews'])

STOP_WORDS = ['but', 'again', 'there', 'about', 'once', 'during', 'out',
'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do',
'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is',
'am', 'or', 'who', 'as', 'will', 'and', 'the', 'from', 'at', 'let',
'and', 'the', 'of', 'to', 'is', 'are', 'their', 'from', 'a', 'in', 'that'
, 'this', 'it', 'on', 'by', 'i', 'still', 'thing', 'even', 'lot', 'see']



def wordcloud(text):
    """
    

    Parameters
    ----------
    One string

    Function: Creates a word cloud for text

    Returns
    -------
    No return

    """

    
    #cloud = wc.WordCloud().generate(text)
    #plt.imshow(cloud)
    #plt.axis(False)

def sentiment_score(text):
    """ Function: sentiment_score
    Parameters: string of text
    Returns: average sentiment score of the words in a string/text
    """
    
    text = text.strip().split()
    total = 0
    for word in text:
        polarity = TextBlob(word).sentiment.polarity
        total += polarity
    return round(total / len(text), 5)

#def clean(text):
#  """
#  Cleans text(punctuation, lowercase, stop words) and returns a list of all words
#  HAS ISSUES, DONT USE
#  """
#  
#  text = text.strip().lower().split(".")
#  clean_text = ''
#  for sentence in text:
#    sentence = sentence.strip()
#    for word in sentence:
#      word = word.strip()
#      if word not in STOP_WORDS:
#        clean_text = clean_text + word
#  
#  return clean_text
        

if __name__ == "__main__":

  df = df.reset_index()
  df = df.drop('index', axis = 1)

  text = ""
  for i in range(len(df)):
    review = df.loc[i, "review"]
    text = text + str(review)

  #cloud = wordcloud(text)

  print(sentiment_score(text))
  #print(df.head(10))

