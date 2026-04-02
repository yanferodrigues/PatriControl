from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,User
from user.models import Usuario
from django.contrib import messages

def user(request):
    nome_usuario_formatado = "" 

    if request.user.is_authenticated:
        usuario = Usuario.objects.filter(user=request.user).first()

        if usuario:
            partes = usuario.user.username.split(".")

            if len(partes) >= 2:
                nome_usuario_formatado = f"{partes[0]} {partes[1]}".title()
            else:
                nome_usuario_formatado = partes[0].title()

    return render(request, "user.html", {
        "nome": nome_usuario_formatado
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        usuario = request.POST.get("email")
        senha = request.POST.get("senha")

        if not usuario or not senha:
            messages.error(request, "Preencha todos os campos")
            return redirect("login")

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha incorretos")
            return render(request,"login.html", {
                "usuario_input": usuario,
            })

    return render(request, "login.html")


def logout_view(request):
    auth_logout(request)
    return redirect("login")

