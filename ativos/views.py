from django.shortcuts import render
from ativos.models import Ativos
from django.db.models import Sum

def novo_ativo(request):
    return render(request, "novo patrimonio.html")

def ativos(request):
    patrimonio = Ativos.objects.all()
    valor_total = patrimonio.aggregate(total = Sum('valor'))['total']

    return render(request, "ativos.html", {
        "patrimonio":patrimonio,
        "valor_total": valor_total
    })

def descricao_ativo(request):
    return render(request, "descricao ativo.html")