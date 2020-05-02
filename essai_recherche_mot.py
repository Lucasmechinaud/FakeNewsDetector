from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='b887d1939c004198a6f027703cb318e6')

# /v2/everything
all_articles = newsapi.get_everything(q='europe')