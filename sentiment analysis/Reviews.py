

import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob




reviews= pd.read_csv("C:\\Users\\rodri\\OneDrive - ISEG\\iseg 22092021\\Iseg\\Master\\2semester\\Programing for Data Science\\trabalho\\reviews.csv.gz", compression= "gzip")

reviews.head()



#Select the variable needed.
reviews = reviews[["comments"]]

#Nr of comments
len(reviews)




#Clear null coments
reviews= reviews.dropna()

#nr of comments w/o null
len(reviews)




#lower case
reviews.astype(str)
reviews["lowerCase"]=reviews["comments"].apply(lambda x: " ".join(word.lower() for word in x.split()))
reviews.head()




#eliminate <br/>
reviews["lowerCase"] = reviews["lowerCase"].str.replace('<br/>', '')




#remove punctuation
reviews["punctuation"] = reviews["lowerCase"].str.replace('[^\w\s]', '')




print(reviews.head())




#remove stop words languages- French, Portuguese, German,...
#Note: stopwords doesnt include all languages 
#I still dont know what to do from this point because of the multiple languages

#languages avalailable for stopwords
stopwords.fileids()




# Do a loop for all the languages to improve?
stop_wordsEn = stopwords.words("english")
stop_wordsGer = stopwords.words("german")
stop_wordsFr = stopwords.words("french")
stop_wordsPt = stopwords.words("portuguese")
stop_wordsEs = stopwords.words("spanish")
stop_wordsGr = stopwords.words("greek")



reviews["w/o_stopwords"]= reviews["punctuation"].apply(lambda x: " ".join(word for word in x.split() if word not in stop_wordsEn))
reviews["w/o_stopwords"]= reviews["w/o_stopwords"].apply(lambda x: " ".join(word for word in x.split() if word not in stop_wordsGer))
reviews["w/o_stopwords"]= reviews["w/o_stopwords"].apply(lambda x: " ".join(word for word in x.split() if word not in stop_wordsFr))
reviews["w/o_stopwords"]= reviews["w/o_stopwords"].apply(lambda x: " ".join(word for word in x.split() if word not in stop_wordsPt))
reviews["w/o_stopwords"]= reviews["w/o_stopwords"].apply(lambda x: " ".join(word for word in x.split() if word not in stop_wordsEs))
reviews["w/o_stopwords"]= reviews["w/o_stopwords"].apply(lambda x: " ".join(word for word in x.split() if word not in stop_wordsGr))
#I noticed that some some stop words from a language remove words from other language
#And this takes a lot of time and memory, my pc almost burned

#nr of words of each comment
reviews["word_count"] = reviews["w/o_stopwords"].apply(lambda x: len(x.split()))

#nr of characters in a comment
reviews["chars_count"] = reviews["w/o_stopwords"].apply(lambda x: len(x))

#average length of words per comment
reviews["avg_len_word"]=reviews["chars_count"]/reviews["word_count"]

#nr of stop words per comment
reviews["stop_word_count"] = reviews["punctuation"].apply(lambda x: len(x.split())) - reviews["word_count"]

#stop words rate per comment
reviews["stop_words_rate"] = reviews["stop_word_count"] /reviews["punctuation"].apply(lambda x: len(x.split())) * 100 

#analyze this shit later, erros spotted due to language and other stuff 
reviews.sort_values(by="stop_words_rate").head(30)



pd.Series(" ".join(reviews["w/o_stopwords"]).split()).value_counts()

words= " ".join(reviews["w/o_stopwords"]).split()


fd= nltk.FreqDist(words)
fd.most_common(30)


#word cloud
wc = WordCloud(background_color= "white", height = 600, width = 400)

wc.generate(words)

wc.to_file("wordcloud_output.png")

#sentiment analysis

blob = TextBlob(words)
sentiment = blob.sentiment.polarity

sentiment



#plots

common = fd.most_common()

fd.plot(20, cumulative = False)



# https://www.youtube.com/watch?v=_jLRKUuBUtY -> Link for translation guide?





