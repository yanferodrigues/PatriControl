from user.models import Usuario
from django.contrib.auth.models import User

def usuario_logado(request):
    nome_usuario_formatado = "" 

    if request.user.is_authenticated:
        usuario = Usuario.objects.filter(user=request.user).first()

        if usuario:
            partes = usuario.user.username.split(".")

            if len(partes) >= 2:
                nome_usuario_formatado = f"{partes[0]} {partes[1]}".title()
            else:
                nome_usuario_formatado = partes[0].title()
            return{
                "usuario":usuario,
                "nome":nome_usuario_formatado
                }

    return {"nome":nome_usuario_formatado}
    