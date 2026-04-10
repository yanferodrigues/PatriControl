from django.shortcuts import render, get_object_or_404, redirect
from ativos.models import Ativos
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



@login_required
def novo_ativo(request):
    if request.method == "POST":
        codigo = request.POST.get("input-codigo-ativo")
        descricao = request.POST.get("input-descricao-ativo")
        chassi = request.POST.get("input-chassi-ativo")
        placa = request.POST.get("input-placa-ativo")
        adesivado = request.POST.get("input-adesivado-ativo") == '1'
        codigo_auxiliar = request.POST.get("input-auxiliar-ativo")
        cor = request.POST.get("input-cor-ativo")
        categoria = request.POST.get("select-categoria-ativo")
        status = request.POST.get("select-status-ativo") == '1'
        detalhamento = request.POST.get("textarea-detalhamento-ativo")
        localizacao = request.POST.get("input-localizacao-ativo")
        responsavel = request.POST.get("input-responsavel-ativo")
        data_incorporacao = request.POST.get("input-data-ativo")
        fornecedor = request.POST.get("input-fornecedor-ativo")
        numero_nf = request.POST.get("input-numero-nf-ativo")
        valor = request.POST.get("input-valor-ativo")
        foto = request.FILES.get("inputFoto")
        nota_fiscal = request.FILES.get("input-nota-fiscal-ativo")
        
        Ativos.objects.create(
            empresa = request.user.extras.empresa,
            foto=foto,
            codigo=codigo,
            descricao=descricao,
            chassi=chassi,
            placa=placa,
            adesivado=adesivado,
            auxiliar=codigo_auxiliar,
            cor=cor,
            categoria=categoria,
            ativo=status,
            detalhamento=detalhamento,
            localizacao=localizacao,
            responsavel=responsavel,
            incorporacao=data_incorporacao,
            fornecedor=fornecedor,
            numero_nota=numero_nf,
            valor=valor,
            nota=nota_fiscal
        )
        
        return redirect("ativos")
            
        
    return render(request, "novo patrimonio.html")

def ativos(request):
    patrimonio_qs = Ativos.objects.filter(empresa=request.user.extras.empresa).order_by("codigo")
    valor_total = patrimonio_qs.aggregate(total=Sum('valor'))['total']
    paginator = Paginator(patrimonio_qs, 50)
    patrimonio = paginator.get_page(request.GET.get('page', 1))

    return render(request, "ativos.html", {
        "patrimonio": patrimonio,
        "patrimonio_todos": patrimonio_qs,
        "valor_total": valor_total,
        "total_count": paginator.count,
    })

def descricao_ativo(request,ativo_id):
    ativo = get_object_or_404(Ativos, id=ativo_id)
    return render(request, "descricao ativo.html", {
        "ativo":ativo,
    })

def apagar_ativo(request, ativo_id):
    ativo = get_object_or_404(Ativos, id=ativo_id, empresa=request.user.extras.empresa)
    if request.method == "POST":
        ativo.delete()
        return redirect("ativos")
    return redirect("descricao-ativo", ativo_id=ativo_id)
    
def buscar_ativo(request):
    ativos = Ativos.objects.filter(empresa=request.user.extras.empresa).order_by("codigo")

    if "buscar" in request.GET:
        busca_ativo = request.GET['buscar']
        ativos = ativos.filter(codigo__icontains=busca_ativo) or ativos.filter(descricao__icontains=busca_ativo)
    if "categoria" in request.GET:
        categoria_ativo = request.GET['categoria']
        if categoria_ativo != 'TODOS':
            ativos = ativos.filter(categoria=categoria_ativo)
    if "status" in request.GET:
        status = request.GET['status']
        if status in ("1", "0"):
            ativos = ativos.filter(ativo=status == '1')
    if "filial" in request.GET:
        filial = request.GET['filial']
        if filial != 'TODOS':
            ativos = ativos.filter(localizacao=filial)

    paginator = Paginator(ativos, 50)
    patrimonio = paginator.get_page(request.GET.get('page', 1))

    return render(request, "buscar_ativo.html", {
        "patrimonio": patrimonio,
        "patrimonio_todos": ativos,
        "total_count": paginator.count,
    })