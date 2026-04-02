from user.models import Usuario
from django.contrib.auth.models import User

def usuario_logado(request):
    usuario = Usuario.objects.get(user=request.user)

    return {
        "usuario":usuario,
    }