from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    name='About'
    return render(request, 'about.html', {'name': name})

def home(request):
    name = 'Dima'
    # html=f'''<!DOCTYPE html>
    # <html lang="en">
    # <head>
    #   <meta charset="utf-8">
    #   <title>Hello World</title>
    #   <link href="style.css" rel="stylesheet" />
    # </head>
    # <body>
    # <h1> Hello {name}! </h1>
    # </body>
    # </html>'''
    # return HttpResponse(html)
    return render(request, 'home.html', {'name': name})
