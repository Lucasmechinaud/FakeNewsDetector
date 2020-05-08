from django import forms
class ArticleUrl(forms.Form):
    Article = forms.CharField(widget= forms.URLInput)