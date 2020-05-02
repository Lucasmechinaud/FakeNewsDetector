from django.db import models
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')
# Create your models here.
#J'essaie de définir la classe qui servira à créer la base de données
#à partir des ressources de Newsapi