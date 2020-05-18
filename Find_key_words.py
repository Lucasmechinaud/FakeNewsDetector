#Le but est ici de tester les fonctions liées à sklearn,pour pouvoir
#obtenir les mots clés à partir de l'article.

import newspaper
import newsapi
from newsapi import NewsApiClient
from newspaper import Article
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import newspaper
import newsapi
from newsapi import NewsApiClient
from newspaper import Article

# Import of Newsapi key
newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')
url = 'https://www.ouest-france.fr/bretagne/maen-roch-35460/deconfinement-en-ille-et-vilaine-des-monuments-historiques-en-sursis-6838807'
# Getting the article title
article = Article(url)
article.download()
article.parse()
article.nlp()
# text_file = open("text_1.txt", "w")
# n = text_file.write(article.text)
# text_file.close()
# lines=['' for i in range(1000)]
# j=0
# with open("text_1.txt","r") as file:
#     for line in file:
#         for word in line.split():
#             if word!="\n":
#                 lines[j]+=word
#                 lines[j]+=' '
#         j=j+1
# file.close()
# text_file_3=open("text_2.txt","w")
# for i in range(len(lines)):
#      if lines[i]!="\n":
#          text_file_3.write(lines[i])
# text_file_3.close()
# text_1=open('text_2.txt')
# titre = article.title
# print(titre)
# #Transforming the title into a txt file
# text_file=open('titre.txt',"w")
# text_file.write(titre)
# text_file.close()
# # Getting the key_words : using sklearn and TfidfVectorizer
# titre=open('titre.txt')
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(titre)
# titre.close()
# # Transforming X into an array : X contains the weight of each word in the title
# X=X.toarray()
# key_words=[0 for i in range(5)] # the table where the key words of the title will be stored.
# indices_max=[0 for i in range(5)] #the table where the indexes of the key words in X will be stored.
# # Let's get the indexes of the 5 key words.
# for j in range(5):
#     ind_max=0
#     for i in range(len(X[0])):
#         # Looking for the word with the most important weight.
#         if X[0][i]>=X[0][ind_max] and len(vectorizer.get_feature_names()[i])>4: #we want the word to be long enough in order to avoid having words such as "to", "the", "us" as key-words.
#             ind_max=i
#     indices_max[j]=ind_max
#     X[0][ind_max]=0 # once we have the most important weight, we put it at 0, so we don't detect it twice.
# # Let's get the key-words
# for i in range(5):
#     key_words[i]=vectorizer.get_feature_names()[indices_max[i]]
#     word_list = list(key_words[i])
#     word_list.insert(0, '+') # we absolutely want those words in the title : putting + before make it mandatory.
#     key_words[i] = ''.join(word_list)
#
# print(key_words)
#
# # Let's look in the data base for articles whose title have all the key words.
# recherche=newsapi.get_everything(qintitle=(key_words[0] + key_words[1]+ key_words[2]))
# print(recherche)
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()
# # Getting the key words
# key_words = article.keywords
# for i in range(5):
#     word_list = list(key_words[i])
#     word_list.insert(0,'+')  # we absolutely want those words in the title : putting + before make it mandatory.
#     key_words[i] = ''.join(word_list)
#     # Finding the articles in the data base that match the key-words (in their core)
# print(key_words)
# all_articles = newsapi.get_everything(q=(key_words[0] + key_words[1] + key_words[2]))
# # Getting the number of articles, ie. the score
# score_1 = all_articles.get("totalResults")
# print(score_1)
# Let's look in the data base for articles whose title have all the key words.
recherche=newsapi.get_everything(qintitle=(key_words[0] + key_words[1]+ key_words[2]))

source = article.source_url
print(source)
if source.find('https://') != -1:
    source=source.replace('https://','')
if source.find('http://') != -1:
    source=source.replace('http://','')
if source.find('www.') != -1:
    source=source.replace('www.','')
if source.find('edition.')!=-1:
    source=source.replace('edition.','')
print(source)
recherche=newsapi.get_everything(domains=source)
print(recherche)