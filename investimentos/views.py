from django.shortcuts import render, redirect
from django.db.models import Sum
from investimentos.models import Investimentos
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
            empresa= request.user.extras.empresa,
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
    investimentos_qs = Investimentos.objects.filter(empresa=request.user.extras.empresa).order_by("codigo")
    valor_total = investimentos_qs.aggregate(total=Sum('valor'))['total']
    paginator = Paginator(investimentos_qs, 50)
    investimentos = paginator.get_page(request.GET.get('page', 1))

    return render(request, "investimentos.html", {
        "investimentos": investimentos,
        "investimentos_todos": investimentos_qs,
        "valor_total": valor_total,
        "total_count": paginator.count,
    })