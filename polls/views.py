from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArticleUrl


# Create your views here.
#la fonction score_creation est pour l'instant en pseudo-code
def score_creation():
    #calcul du score...

    score = 75
    return(locals())
def submit_article(request):
    form = ArticleUrl(request.POST)
    return (render(request, 'polls/submit_article.html', locals()))

def send_results(request):
    form = ArticleUrl(request.POST)
    if form.is_valid():
        article = form.cleaned_data['Article']
    score = score_creation().get('score')
    if score >= 90:
        return(render(request,'polls/results_positive.html',locals()))
    if score>70 and score <90:
        return(render(request,'polls/results_medium.html',locals()))
    else:
        return (render(request, 'polls/results_negative.html', locals()))
