from django.shortcuts import render
from investimentos.models import Investimentos
from ativos.models import Ativos
from django.db.models import Sum
from django.http import JsonResponse

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
    quantidade_veiculos = int(len(Ativos.objects.filter(categoria = "VEÍCULOS")))
    quantidade_maquinas = int(len(Ativos.objects.filter(categoria = "MÁQUINAS E IMPLEMENTOS")))
    quantidade_informatica = int(len(Ativos.objects.filter(categoria = "INFORMÁTICA E COMUNICAÇÃO")))
    quantidade_equipamentos = int(len(Ativos.objects.filter(categoria = "EQUIPAMENTOS DIVERSOS")))
    quantidade_moveis = int(len(Ativos.objects.filter(categoria = "MÓVEIS E UTENSÍLIOS")))
    quantidade_imoveis = int(len(Investimentos.objects.all()))

    data = {
        "valores": [quantidade_veiculos, quantidade_equipamentos,quantidade_maquinas,quantidade_informatica,quantidade_moveis,quantidade_imoveis]
    }

    return JsonResponse(data)