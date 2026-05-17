from django.shortcuts import render
from django.http import HttpResponse
import random

def hello(request):
    return HttpResponse("Hello World")

def drawn_number(request):
    random_num = random.randint(1, 100)
    answer = f"Drawn number: {random_num}"
    return HttpResponse(answer)