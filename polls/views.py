from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return render(request, 'polls/accueil.html', locals())
# Create your views here.
