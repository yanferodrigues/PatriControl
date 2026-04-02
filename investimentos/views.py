from django.shortcuts import render, redirect
from django.db.models import Sum
from investimentos.models import Investimentos
from django.contrib.auth.decorators import login_required

@login_required
def investimentos(request):
    return render(request, "investimentos.html")

def novo_investimento(request):

    if request.method == "POST":
        codigo = request.POST.get("input-codigo-investimento")
        descricao = request.POST.get("input-descricao-investimento")
        status = request.POST.get("select-status-investimento") == '1'
        detalhamento = request.POST.get("textarea-detalhamento-investimento")
        localizacao = request.POST.get("input-localizacao-investimento")
        data = request.POST.get("input-data-investimento")
        valor = request.POST.get("input-valor-investimento")

        Investimentos.objects.create(
            codigo=codigo,
            descricao=descricao,
            ativo=status,
            detalhamento=detalhamento,
            localizacao=localizacao,
            data=data,
            valor=valor
        )

        return redirect("investimentos")
    
    return render(request, "novo investimento.html")

def investimentos(request):
    investimentos = Investimentos.objects.all()
    valor_total = investimentos.aggregate(total = Sum('valor'))['total']

    return render(request, "investimentos.html", {
        "investimentos":investimentos,
        "valor_total": valor_total
    })