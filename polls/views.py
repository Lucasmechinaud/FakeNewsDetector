from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleUrl
import newsapi
from newsapi import NewsApiClient
from newspaper import Article

newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')

# Create your views here.
#la fonction score_creation est pour l'instant en pseudo-code
def score_creation(request):
    form = ArticleUrl(request.POST)
    if form.is_valid():
        url = form.cleaned_data['Article']
        article = Article(url)
        #On calcule le score une première fois avec le module newspaper3k
        article.download()
        article.parse()
        article.nlp()
        key_words = article.keywords
        all_articles = newsapi.get_everything(q=(
                    key_words[0] and key_words[1] and key_words[2] and key_words[3] and key_words[4] and key_words[
                5] and key_words[6] and key_words[7] and key_words[8] and key_words[9] and key_words[10] and key_words[
                        11] and key_words[12] and key_words[13]))
        Total_number = all_articles.get("totalResults")
        score_1=Total_number
        #On calcule le second score avec le module sklearn

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
