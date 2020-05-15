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

newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')

url = 'https://www.bbc.com/news/health-52674739'
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
titre = article.title
print(titre)
text_file=open('titre.txt',"w")
text_file.write(titre)
text_file.close()
tit=open('titre.txt')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tit)
tit.close()
X=X.toarray()
key_words=[0 for i in range(5)]
indices_max=[0 for i in range(5)]
for j in range(5):
    ind_max=0
    for i in range(len(X[0])):
        if X[0][i]>=X[0][ind_max] and len(vectorizer.get_feature_names()[i])>4:
            ind_max=i
    indices_max[j]=ind_max
    X[0][ind_max]=0
for i in range(5):
    key_words[i]=vectorizer.get_feature_names()[indices_max[i]]
    word_list = list(key_words[i])
    word_list.insert(0, '+')
    key_words[i] = ''.join(word_list)

print(key_words)

recherche=newsapi.get_everything(qintitle=(key_words[0] + key_words[1])+ key_words[2])
print(recherche)