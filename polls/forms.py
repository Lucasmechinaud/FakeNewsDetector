from django import forms
class ArticleUrl(forms.Form):
    Article = forms.URLField()
