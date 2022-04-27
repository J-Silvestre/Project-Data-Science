

import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob




reviews= pd.read_csv("C:\\Users\\rodri\\OneDrive - ISEG\\iseg 22092021\\Iseg\\Master\\2semester\\Programing for Data Science\\trabalho\\reviews.csv.gz", compression= "gzip")





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
#This code takes a lot of time to run
stop_wordsEn = stopwords.words("english")
stop_wordsGer = stopwords.words("german")
stop_wordsFr = stopwords.words("french")
stop_wordsPt = stopwords.words("portuguese")
stop_wordsEs = stopwords.words("spanish")
stop_wordsGr = stopwords.words("greek")


#removing stop words for each language
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

# erros spotted due to language and other stuff 
reviews.sort_values(by="stop_words_rate").head(30)

#not working because of the empty values i think
"""
def comment_average(x):
    words = x.split()
    return sum(len(word) for word in words)/ len(words)
"""
#average length of words per comment, does the same thing as the function above
reviews["avg_len_word"]=reviews["chars_count"]/reviews["word_count"]

#nr of stop words per comment
reviews["stop_word_count"] = reviews["punctuation"].apply(lambda x: len(x.split())) - reviews["word_count"]

#stop words rate per comment
reviews["stop_words_rate"] = reviews["stop_word_count"] /reviews["punctuation"].apply(lambda x: len(x.split())) * 100 


#Where i found the missing values and comments with just punctuation
reviews.sort_values(by="stop_words_rate").tail(30)


#gives an overview of how the file looks like after all transformations
reviews.head()

#removes does empty spaces
Comments_final =reviews.dropna()
#Comments_final.sort_values(by="stop_words_rate").tail(30)

#provides some statistics
Comments_final.describe()


#Gives a list with all the words sorted by counting
pd.Series(" ".join(reviews["w/o_stopwords"]).split()).value_counts()



#stores the words in an object
words= " ".join(reviews["w/o_stopwords"]).split()

#Getting the top x most common words
fd= nltk.FreqDist(words)
fd.most_common(30)

### Word Cloud ------------------------------

# creating the word cloud
wc = WordCloud(background_color= "white", height = 600, width = 400)

wc.generate(words)
#adding the world cloud to file
wc.to_file("wordcloud_output.png")


### Sentiment analysis ----------------------

#This also takes a lot of time to run and im not sure if its working properly

#reorganized index
Index=[]
for i in range(len(Comments_final["w/o_stopwords"])):
    Index.append(i)
    
Comments_final["Index"]= Index
Comments_final=Comments_final.set_index("Index")



#creating a function to get the polarity of the comments
Comments_final["w/o_stopwords"]=Comments_final["w/o_stopwords"].astype('str')
def get_polarity(text):
    return TextBlob(text).sentiment.polarity

#applying the fucntion
Comments_final['Polarity'] = Comments_final['w/o_stopwords'].apply(get_polarity)


#adding columns with the polarity score as negative, neutral or positive
Comments_final['Sentiment_Type']=''
Comments_final.loc[Comments_final.Polarity>0,'Sentiment_Type']='POSITIVE'
Comments_final.loc[Comments_final.Polarity==0,'Sentiment_Type']='NEUTRAL'
Comments_final.loc[Comments_final.Polarity<0,'Sentiment_Type']='NEGATIVE'


#grouping by listings id to get the mean polarity of all coments for each listing
CommentScore=Comments_final[["listing_id","Polarity"]]
CommentScore=CommentScore.groupby(["listing_id"]) 
Score=CommentScore["Polarity"].mean()
Score.describe()

Score.to_csv("sentiment.csv")

#plots / visualization -----------------------


#most common words
common = fd.most_common()

fd.plot(20, cumulative = False)


#bar plot for sentiment analysis
Comments_final.Sentiment_Type.value_counts().plot(kind='bar',title="Sentiment Analysis")

# https://www.youtube.com/watch?v=_jLRKUuBUtY -> Link for translation guide?





