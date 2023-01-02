from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username1=request.POST['username']
        password1=request.POST['password']
        from django.contrib import auth
        user=auth.authenticate(username=username1, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')

    else:
        return render(request, 'login.html')