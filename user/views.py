from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,User
from user.models import Usuario
from django.contrib import messages

def user(request):
    if request.user.is_authenticated:
        user = request.user
        usuario = Usuario.objects.get(user = user)
        nome_usuario = usuario.user.username.split(".")
        nome_usuario_formatado = f"{nome_usuario[0]} {nome_usuario[1]}".title()

    return render(request,"user.html", {
        "usuario":usuario,
        "nome_usuario":nome_usuario_formatado
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if not email or not senha:
            messages.error(request, "Preencha todos os campos")
            return redirect("login")

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha incorretos")
            return render(request,"login.html", {
                "email": email,
            })

    return render(request, "login.html")


def logout_view(request):
    auth_logout(request)
    return redirect("login")

