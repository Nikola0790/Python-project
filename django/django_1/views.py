from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Band, Album
import random

def hello(request):
    return HttpResponse("Hello World")

def drawn_number(request):
    random_num = random.randint(1, 100)
    answer = f"Drawn number: {random_num}"
    return HttpResponse(answer)

def random_max_number(request, max_num):
    random_num = random.randint(0, max_num)
    answer = f"The user entered the value {max_num}. The following number was drawn: {random_num}"
    return HttpResponse(answer)

def random_number(request, min_number, max_number):
    random_num = random.randint(min_number, max_number)
    answer = f"The user entered the values {min_number} and {max_number}. The following number was drawn: {random_num}"
    return HttpResponse(answer)

def hello_name(request, name):
    return HttpResponse(f"Hello {name}")

def articles(request):
    articles = Article.objects.filter(status="in writing")
    context = {
        'articles': articles
    }

    return render(request, 'django_1/articles.html', context)

def bands_albums(request):
    # prefetch_related tells Django: "Hey, I am about to loop through all these bands, their albums, and their songs. 
    # Go to the database right now, grab all of them in bulk, and join them together in Python's memory."

    #Django performs exactly 3 highly optimized queries, no matter how many hundreds of bands, albums, or songs you have:
        #SELECT * FROM django_1_band; (Get all bands)
        #SELECT * FROM django_1_album WHERE band_id IN (...); (Get all albums for those bands)
        #SELECT * FROM django_1_song WHERE album_id IN (...); (Get all songs for those albums)
        
    # The double underscore (__) is Django's syntax for "look deeper into the relationship chain." 
    # So 'album_set__song_set' literally translates to: "Follow the band's album set, and then follow those albums' song sets."
    bands = Band.objects.prefetch_related('album_set__song_set').all()
    context = {
        'bands': bands,
    }

    return render(request, 'django_1/bands.html', context)