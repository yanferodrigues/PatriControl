from django.shortcuts import render
from investimentos.models import Investimentos
from ativos.models import Ativos
from django.db.models import Sum

def dashboard(request):
    ativos = Ativos.objects.all()
    investimentos = Investimentos.objects.all()
    valor_total_ativos = ativos.aggregate(total = Sum("valor"))["total"]
    valor_total_investimentos = investimentos.aggregate(total = Sum("valor"))["total"]
    
    return render(request,"index.html", {
        "ativos":ativos,
        "investimentos":investimentos,
        "valor_total_ativos":valor_total_ativos,
        "valor_total_investimentos":valor_total_investimentos
    })
