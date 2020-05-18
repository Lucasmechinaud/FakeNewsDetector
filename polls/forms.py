from django import forms
#Creation of a form
class ArticleUrl(forms.Form):
    Article = forms.URLField()
