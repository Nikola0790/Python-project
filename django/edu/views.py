from django.shortcuts import render
from django.http import HttpResponse

def show_number(request, number):
    answer = """
            <html>
                <body>
                    <p>The answer is {}!</p>
                </body>
            </html>
            """.format(number)
    return HttpResponse(answer)