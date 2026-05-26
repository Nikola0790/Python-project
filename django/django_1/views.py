from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View
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

@csrf_exempt
def set_session(request):
    request.session['counter'] = 0
    return HttpResponse('<p>Counter session set.</p>')

@csrf_exempt
def show_session(request):
    if 'counter' in request.session:
        session = request.session.get('counter')
        request.session['counter'] += 1
        return HttpResponse(f"<h1>Contents of the session: {session}.</h1>")
    else:
        return  HttpResponse("<p>No counter data in session!</p>")
    
@csrf_exempt
def delete_session(request):
    if 'counter' in request.session:
        del request.session['counter']
    
    return HttpResponse('<p>Counter session removed.</p>')

@csrf_exempt
def my_view(request):
    FORM = """<form action="" method="POST">
        <label>
            Name:
            <input type="text" name="name">
        </label>
        <input type="submit">
        </form>
        """
    if request.method == 'GET':
        if 'logged_user' in request.session:
            return HttpResponse(f"<p>Welcome {request.session.get('logged_user')}</p>")
        else:    
            return HttpResponse(FORM)
    elif request.method == 'POST':
        request.session['logged_user'] = request.POST.get('name')
        return HttpResponse(f"<p>Welcome {request.session.get('logged_user')}</p>")

@csrf_exempt
def add_to_session(request):
    FORM = """<form action="#" method="POST">
        <label>
            Key:
            <input type="text" name="key">
        </label>
        <label>
            Value:
            <input type="text" name="value">
        </label>
        <input type="submit">
        </form>
        """
    if request.method == "GET":
        return HttpResponse(FORM)
    elif request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        request.session[key] = value
    return HttpResponse(f"Key Value pair is added. <a href='add-to-session/'>Add new</a>")

def show_all_session(request):
    if request.method == 'GET':
        html_content = "<h2>Your Session Data:</h2><ul>"
        if not request.session.items():
            html_content += "<li>No data found in the current session.</li>"
        else:
            for key, value in request.session.items():
                html_content += f"<li><strong>{key}:</strong> {value}</li>"
        html_content += "</ul>"
            
    return HttpResponse(html_content)

def set_cookie(request):
    response = HttpResponse('Setting cookies')
    response.set_cookie("User", "Nikola")
    return response

def show_cookie(request):
    if 'User' in request.COOKIES:
        return HttpResponse(request.COOKIES.get('User'))
    else:
        return HttpResponse("Cookie User doesn't exist.")

def delete_cookie(request):
    if 'User' in request.COOKIES:
        response = HttpResponse('Cookie deleted.')
        response.delete_cookie('User')
        return response
    
@csrf_exempt
def add_to_cookie(request):
    FORM = """<form action="#" method="POST">
        <label>
            Key:
            <input type="text" name="key">
        </label>
        <label>
            Value:
            <input type="text" name="value">
        </label>
        <input type="submit" name="conversionType">
        </form>
        """
    if request.method == 'GET':
        return HttpResponse(FORM)
    elif request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        response = HttpResponse(f"Cookie added. <a href=''>Add new cookie.</a>")
        response.set_cookie(key, value)
        return response
    
def show_all_cookies(request):
    if request.method == 'GET':
        html_content = "<ul>"
        for key, value in request.COOKIES.items():
            html_content += f"<li>Key: {key} - Value: {value}</li>"
        html_content += "</ul>"
    return HttpResponse(html_content)

@method_decorator(csrf_exempt, name='dispatch')
class ViewClassExercise(View):
    FORM = """
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
    def get(self, request):
        return HttpResponse(self.FORM)
    def post(self, request):
        name = request.POST.get('user_name')
        surname = request.POST.get('user_surname')

        if name is not None and surname is not None:
            result = f"Welcome, {name} {surname}." + self.FORM
            return HttpResponse(result)
        
        return HttpResponse(self.FORM)
    
class ViewBands(View):
    def get(self, request):
        bands = Band.objects.all()
        context = {
            'bands': bands,
        }
        return render(request, 'django_1/bands2.html', context)
    
    def post(self, request):
        name = request.POST.get('name')
        year = request.POST.get('year')
        is_active = request.POST.get('is_active') == 'true'
        genre = request.POST.get('genre')

        if name and year and genre:
            Band.objects.create(name=name, year=year, still_active=is_active, genre=int(genre))
            messages.success(request, f'The band "{name}" was saved successfully to the database!')
            
            return redirect(request.path)
    
        messages.error(request, 'All fields are required.')
        bands = Band.objects.all()
        return render(request, 'django_1/bands2.html', {'bands': bands})