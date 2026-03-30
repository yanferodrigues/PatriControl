from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def user(request):
    return render(request,"user.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        user = authenticate(request, username=email, password=senha)
        if user is not None :
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha incorretos")
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("login")