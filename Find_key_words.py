#Le but est ici de tester les fonctions liées à sklearn,pour pouvoir
#obtenir les mots clés à partir de l'article.

import newspaper
import newsapi
from newsapi import NewsApiClient
from newspaper import Article

newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')

url = 'http://www.legorafi.fr/2020/04/16/manuel-valls-ecope-dune-amende-pour-non-respect-du-confinement-apres-avoir-dormi-sur-le-paillasson-demmanuel-macron/'
article = Article(url)
article.download()
article.parse()
article.nlp()
text_file = open("text_1.txt", "w")
n = text_file.write(article.title)
text_file.close()
text_1=open('text_1.txt')
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text_1)
print(X)
print(vectorizer.get_feature_names())
X=X.toarray()
key_words=[0 for i in range(10)]
indices_max=[0 for i in range(10)]
for j in range(10):
    ind_max=0
    for i in range(len(X[0])):
        if X[0][i]>=X[0][ind_max]:
            ind_max=i
    indices_max[j]=ind_max
    X[0][ind_max]=0
for i in range(10):
    key_words[i]=vectorizer.get_feature_names()[indices_max[i]]
print(key_words)



