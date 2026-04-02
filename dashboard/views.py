from django.shortcuts import render, redirect
from investimentos.models import Investimentos
from ativos.models import Ativos
from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from user.models import Usuario

@login_required
def dashboard(request):

    ativos = Ativos.objects.all()
    investimentos = Investimentos.objects.all()
    valor_total_ativos = ativos.aggregate(total = Sum("valor"))["total"]
    valor_total_investimentos = investimentos.aggregate(total = Sum("valor"))["total"]
    ativos_ultimos = Ativos.objects.all().order_by("-id")[:7]
    
    return render(request,"index.html", {
        "ativos":ativos,
        "ativos_ultimos":ativos_ultimos,
        "investimentos":investimentos,
        "valor_total_ativos":valor_total_ativos,
        "valor_total_investimentos":valor_total_investimentos
    })

def grafico(request):

    categorias = [
        "VEÍCULOS",
        "EQUIPAMENTOS DIVERSOS",
        "MÁQUINAS E IMPLEMENTOS",
        "INFORMÁTICA E COMUNICAÇÃO",
        "MÓVEIS E UTENSÍLIOS",
        "EQUIPAMENTOS OFICINA",
        "EQUIPAMENTOS UBG",
        "EQUIPAMENTOS UBA",
        "AERONAVES"
    ]

    labels = []
    valores = []

    for categoria in categorias:
        quantidade = Ativos.objects.filter(categoria=categoria).count()

        labels.append(categoria.capitalize())  # deixa bonito no gráfico
        valores.append(quantidade)

    # imóveis separado
    labels.append("Imóveis")
    valores.append(Investimentos.objects.count())

    return JsonResponse({
        "labels": labels,
        "valores": valores
    })