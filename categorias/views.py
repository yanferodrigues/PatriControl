from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from categorias.models import CategoriaOperacional


@login_required
def nova_categoria(request):
    if request.method == "POST":
        nome = request.POST.get("input-nome-categoria", "").strip().upper()
        if nome:
            CategoriaOperacional.objects.create(
                empresa=request.user.extras.empresa,
                nome=nome,
            )
        return redirect("categorias")
    return render(request, "nova categoria.html")


@login_required
def categorias(request):
    cats = CategoriaOperacional.objects.filter(
        empresa=request.user.extras.empresa
    ).order_by("nome")
    return render(request, "categorias.html", {"categorias": cats})


@login_required
def apagar_categoria(request, categoria_id):
    cat = get_object_or_404(CategoriaOperacional, id=categoria_id, empresa=request.user.extras.empresa)
    if request.method == "POST":
        cat.delete()
    return redirect("categorias")
