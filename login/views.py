from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg

def cadastro(request):
    if request.method == "GET":
        return render(request, 'login/cadastro.html', {'it': False})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'login/cadastro.html', {'it': True})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return render(request, 'login/login.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login/login.html', {'it': False})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            lg(request, user)
            return redirect('reader:scan')
        else:
            return render(request, 'login/login.html', {'it': True})