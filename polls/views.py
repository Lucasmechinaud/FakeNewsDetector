from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleUrl
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
        # Finding the articles in the data base that match the key-words (in their core)
        all_articles = newsapi.get_everything(q=(
                    key_words[0] and key_words[1] and key_words[2] and key_words[3] and key_words[4] and key_words[
                5] and key_words[6] and key_words[7] and key_words[8] and key_words[9] and key_words[10] and key_words[
                        11] and key_words[12] and key_words[13]))
        # Getting the number of articles
        Total_number = all_articles.get("totalResults")
        # That's the first score
        score_1=Total_number
        # Let's calculate the score with a "manual" method  : key words in the title.

        score=(score_1+score_2)/2

    return(locals())
def submit_article(request):
    form = ArticleUrl(request.POST)
    return (render(request, 'polls/submit_article.html', locals()))

def send_results(request):
    score = score_creation(request).get('score')
    if score >= 90:
        return(render(request,'polls/results_positive.html',locals()))
    if score>70 and score <90:
        return(render(request,'polls/results_medium.html',locals()))
    else:
        return (render(request, 'polls/results_negative.html', locals()))
