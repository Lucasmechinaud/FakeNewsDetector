from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')
#Le but ici est de créer une fonction qui compte le nombre d'articles comportant le groupe de mots clés
#obtenus à partir de l'article testé. IL reste néanmoins à savoir:
# - sous quelle forme sont renvoyés les mots clés

#le squelette de la fonction serait le suivant:
#def compare():
all_articles = newsapi.get_everything(q='France')

Total_number= all_articles.get("totalResults")

#definition des seuils:
if Total_number <= First_threshold:
    score = first_score
else:
    #etc etc
return(score)