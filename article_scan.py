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
print(article.text)

# key_words = article.keywords
# print(key_words)
#
# all_articles = newsapi.get_everything(q=(key_words[0] and key_words[1] and key_words[2] and key_words[3] and key_words[4] and key_words[5] and key_words[6] and key_words[7] and key_words[8] and key_words[9] and key_words[10] and key_words[11] and key_words[12] and key_words[13]))
# print(all_articles)
# Total_number= all_articles.get("totalResults")