from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
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

def bands_albums(request, number):
    # prefetch_related tells Django: "Hey, I am about to loop through all these bands, their albums, and their songs. 
    # Go to the database right now, grab all of them in bulk, and join them together in Python's memory."

    #Django performs exactly 3 highly optimized queries, no matter how many hundreds of bands, albums, or songs you have:
        #SELECT * FROM django_1_band; (Get all bands)
        #SELECT * FROM django_1_album WHERE band_id IN (...); (Get all albums for those bands)
        #SELECT * FROM django_1_song WHERE album_id IN (...); (Get all songs for those albums)

    # The double underscore (__) is Django's syntax for "look deeper into the relationship chain." 
    # So 'album_set__song_set' literally translates to: "Follow the band's album set, and then follow those albums' song sets."
    # bands = Band.objects.prefetch_related('album_set__song_set').all()

    band = Band.objects.get(id=number)
    context = {
        'band': band,
    }

    return render(request, 'django_1/bands.html', context)

def number_range_view(request):
    if request.method == 'GET':
        start_num = request.GET.get('start')
        end_num = request.GET.get('end')
        numbers = range(int(start_num), int(end_num))
        context = {
            "numbers": numbers,
        }
        return render(request, 'django_1/numbers.html', context)
    else:
        raise Http404

@csrf_exempt
def form(request):
    form_html = """
        <form action="" method="post">
            <label>
                Name:
                <input type="text" name="user_name">
            </label>
            <label>
                Surname:
                <input type="text" name="user_surname">
            </label>
            <button type="submit">Submit</button>
        </form>
        """
    if request.method == 'GET':
        return HttpResponse(form_html)
    elif request.method == 'POST':
        name = request.POST.get('user_name')
        surname = request.POST.get('user_surname')

        if name is not None and surname is not None:
            result = f"Hello, {name} {surname}." + form_html
            return HttpResponse(result)
        else:
            html = "<html><body>Error!</body></html>"
        return HttpResponse(html)
    
@csrf_exempt
def temp_convert(request):
    form_html = """
        <form action="" method="POST">
            <label>
                Temperature:
                <input type="number" min="0.00" step="0.01" name="degrees">
            </label>
            <input type="submit" name="conversionType" value="celcToFahr">
            <input type="submit" name="conversionType" value="FahrToCelc">
        </form>
        """
    if request.method == 'GET':
        return HttpResponse(form_html)
    elif request.method == "POST":
        degrees = request.POST.get('degrees')
        conversion_type = request.POST.get('conversionType')

        if degrees is not None and conversion_type is not None:
            if conversion_type == "FahrToCelc":
                result = f"{(int(degrees) - 32) / 1.8}" + form_html
                return HttpResponse(result)
            else:
                result = f"{int(degrees) * 1.8 + 32}" + form_html
                return HttpResponse(result)
        else: 
            html = "<html><body>Error!</body></html>"
            return HttpResponse(html)
