import newspaper
import newsapi
from newsapi import NewsApiClient
from newspaper import Article

newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')

url = 'https://edition.cnn.com/2020/05/15/politics/trump-2016-instincts-pandemic-second-term/index.html'
article = Article(url)
article.download()
article.parse()
article.nlp()

source = article.source_url
print(source)

text_file = open("source.txt", "w")
n = text_file.write(article.source_url)
text_file.close()
letters=['' for i in range(1000)]
j=0
with open("source.txt","r") as file:
    for line in file:
        i=0
        for ch in line:
            letters[i]+=ch;
            i=i+1
        j=j+1
file.close()
text_file = open("source_sans_https",'w')
i=0
while letters[i]!='':
    if letters[i]=='w' and letters[i+1]=='w' and letters[i+2]=='w' and letters[i+3]=='.':
        j=4
        while letters[i+j]!='':
            n= text_file.write(letters[i+j])
            j=j+1
    i=i+1
text_file.close()
source=open("source_sans_https",'r')
url_a_rechercher=source.readline()
print(url_a_rechercher)
recherche=newsapi.get_everything(domains=url_a_rechercher)
print(recherche)
# key_words = article.keywords
# print(key_words)
#
# all_articles = newsapi.get_everything(q=(key_words[0] and key_words[1] and key_words[2] and key_words[3] and key_words[4] and key_words[5] and key_words[6] and key_words[7] and key_words[8] and key_words[9] and key_words[10] and key_words[11] and key_words[12] and key_words[13]))
# print(all_articles)
# Total_number= all_articles.get("totalResults")