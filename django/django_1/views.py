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
    band = Band.objects.get(name='Metallica')
    bands_albums = band.album_set.all()
    context = {
        'albums': bands_albums
    }

    return render(request, 'django_1/bands.html', context)