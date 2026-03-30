from django.shortcuts import render, get_object_or_404
from ativos.models import Ativos
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required
def novo_ativo(request):
    return render(request, "novo patrimonio.html")

def ativos(request):
    patrimonio = Ativos.objects.all()
    valor_total = patrimonio.aggregate(total = Sum('valor'))['total']

    return render(request, "ativos.html", {
        "patrimonio":patrimonio,
        "valor_total": valor_total
    })

def descricao_ativo(request,ativo_id):
    ativo = get_object_or_404(Ativos, id=ativo_id)
    return render(request, "descricao ativo.html", {
        "ativo":ativo,
    })