from django.shortcuts import render, redirect
from investimentos.models import Investimentos
from ativos.models import Ativos
from django.db.models import Sum
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from user.models import Usuario

@login_required
def dashboard(request):

    ativos = Ativos.objects.filter(empresa = request.user.extras.empresa)
    investimentos = Investimentos.objects.filter(empresa = request.user.extras.empresa)
    valor_total_ativos = ativos.aggregate(total = Sum("valor"))["total"]
    valor_total_investimentos = investimentos.aggregate(total = Sum("valor"))["total"]
    ativos_ultimos = ativos.order_by("-id")[:7]
    valor_total_depreciado = sum(
        a.valor_depreciado for a in ativos if a.valor_depreciado is not None
    )

    return render(request,"index.html", {
        "ativos":ativos,
        "ativos_ultimos":ativos_ultimos,
        "investimentos":investimentos,
        "valor_total_ativos":valor_total_ativos,
        "valor_total_investimentos":valor_total_investimentos,
        "valor_total_depreciado": valor_total_depreciado if valor_total_depreciado else None,
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
        quantidade = Ativos.objects.filter(categoria=categoria, empresa = request.user.extras.empresa).count()

        labels.append(categoria.capitalize())  # deixa bonito no gráfico
        valores.append(quantidade)

    # imóveis separado
    labels.append("Imóveis")
    valores.append(Investimentos.objects.filter(empresa = request.user.extras.empresa).count())

    return JsonResponse({
        "labels": labels,
        "valores": valores
    })