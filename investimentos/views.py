from django.shortcuts import render
from django.db.models import Sum
from investimentos.models import Investimentos
from django.contrib.auth.decorators import login_required

@login_required
def investimentos(request):
    return render(request, "investimentos.html")

def novo_investimento(request):
    return render(request, "novo investimento.html")

def investimentos(request):
    investimentos = Investimentos.objects.all()
    valor_total = investimentos.aggregate(total = Sum('valor'))['total']

    return render(request, "investimentos.html", {
        "investimentos":investimentos,
        "valor_total": valor_total
    })