from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleUrl
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

# Create your views here.
def score_creation(request):
    form = ArticleUrl(request.POST)
    if form.is_valid():
        url = form.cleaned_data['Article']
        article = Article(url)
        # Let's calculate the score with an "automatic" method : key words in the whole article
        # Getting the article
        article.download()
        article.parse()
        article.nlp()
        # Getting the key words
        key_words = article.keywords
        for i in range(5):
            word_list = list(key_words[i])
            word_list.insert(0,'+')  # we absolutely want those words in the article : putting + before make it mandatory.
            key_words[i] = ''.join(word_list)
        # Finding the articles in the data base that match the three first key-words (in their core)
        all_articles = newsapi.get_everything(q=(key_words[0] + key_words[1] + key_words[2] + key_words[3] + key_words[4]))
        # Getting the number of articles, ie. the score
        score_1 = all_articles.get("totalResults")
        # Let's calculate the score with a "manual" method  : key words in the title.
        titre = article.title
        # Transforming the title into a txt file
        text_file = open('titre.txt', "w")
        text_file.write(titre)
        text_file.close()
        # Getting the key_words : using sklearn and TfidfVectorizer
        titre = open('titre.txt')
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(titre)
        titre.close()
        # Transforming X into an array : X contains the weight of each word in the title
        X = X.toarray()
        key_words_2 = [0 for i in range(5)]  # the table where the key words of the title will be stored.
        indices_max = [0 for i in range(5)]  # the table where the indexes of the key words in X will be stored.
        # Let's get the indexes of the 5 key words.
        for j in range(5):
            ind_max = 0
            for i in range(len(X[0])):
                # Looking for the word with the most important weight.
                if X[0][i] >= X[0][ind_max] and len(vectorizer.get_feature_names()[
                                                        i]) > 4:  # we want the word to be long enough in order to avoid having words such as "to", "the", "us" as key-words.
                    ind_max = i
            indices_max[j] = ind_max
            X[0][ind_max] = 0  # once we have the most important weight, we put it at 0, so we don't detect it twice.
        # Let's get the key-words
        for i in range(5):
            key_words_2[i] = vectorizer.get_feature_names()[indices_max[i]]
            word_list = list(key_words_2[i])
            word_list.insert(0,
                             '+')  # we absolutely want those words in the title : putting + before make it mandatory.
            key_words_2[i] = ''.join(word_list)
        # Let's look in the data base for articles whose title have all the key words.
        recherche = newsapi.get_everything(qintitle=(key_words_2[0] + key_words_2[1] + key_words_2[2]))
        score_2 = recherche.get("totalResults")
        score=(score_1+score_2)/2
        score =score*100/500
        if score >100:
            score =100
        # Let's find if the source can be trusted
        source = article.source_url
        # Remodeling the source url in order to match the format of newsapi
        if source.find('https://') != -1:
            source = source.replace('https://', '')
        if source.find('http://') != -1:
            source = source.replace('http://', '')
        if source.find('www.') != -1:
            source = source.replace('www.', '')
        if source.find('edition.') != -1: # especially because cnn is sometimes referenced as edition.cnn
            source = source.replace('edition.', '')
        # Finding all the articles from that source
        recherche_source = newsapi.get_everything(domains=source)
        number_of_article=recherche_source.get("totalResults")
        if number_of_article > 500:
            score = 100
    return(locals())

def submit_article(request):
    form = ArticleUrl(request.POST)
    return (render(request, 'polls/submit_article.html', locals()))

def send_results(request):
    score = score_creation(request).get('score')
    if score >= 100:
        return(render(request,'polls/results_positive.html',locals()))
    if score>70 and score <100:
        return(render(request,'polls/results_medium.html',locals()))
    else:
        return (render(request, 'polls/results_negative.html', locals()))
