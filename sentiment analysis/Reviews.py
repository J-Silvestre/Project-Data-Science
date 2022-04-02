

import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords




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


stopwords.fileids()




stop_wordsEn = stopwords.words("english")
stop_wordsGer = stopwords.words("german")
stop_wordsFr = stopwords.words("french")
stop_wordsPt = stopwords.words("portuguese")
stop_wordsEs = stopwords.words("spanish")



reviews["punctuation"].apply(lambda x: " ".join(word for word in x.split() if word not in stop_wordsEn))


pd.Series(" ".join(reviews["punctuation"]).split() ).value_counts()






