# FakeNewsDetector

Our Fake News Detector is based on three different scores:
- an "automatic" score that uses the method key_word of "newspaper3k"
- a "manual" score where the key words are found according to their weight in the title.
- a score that expresses the fiability of the source

How to use our project ?
- download all the files on our github
- in a prompt : py manage.py runserver
- go to : http://localhost:8000/submit_article/
- submit your article

For our project, we used :
- django
- newspaper
- sklearn
- newsapi

This is version 1.0.

Authors : Lucas Méchinaud, Nolwenn Smith
