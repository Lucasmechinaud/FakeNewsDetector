#Le but est ici de tester les fonctions liées à sklearn,pour pouvoir
#obtenir les mots clés à partir de l'article.
text_1 = open('test_key_word.txt')
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text_1)
print(X)
print(vectorizer.get_feature_names())