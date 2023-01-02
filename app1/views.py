from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def Home(request):
    return render(request, 'a.html', {'titles' : 'Django', 'link' : 'http://127.0.0.1:8000/'})

def Profile(request):
    return render(request, 'a.html', {'titles' : 'profile', 'link' : 'http://127.0.0.1:8000/'})

def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a*b+2
    return render(request, 'output.html', {'result' : c})