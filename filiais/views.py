from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from filiais.models import Filial


@login_required
def nova_filial(request):
    if request.method == "POST":
        nome = request.POST.get("input-nome-filial", "").strip().upper()
        if nome:
            Filial.objects.create(
                empresa=request.user.extras.empresa,
                nome=nome,
            )
        return redirect("filiais")
    return render(request, "nova filial.html")


@login_required
def filiais(request):
    filiais_qs = Filial.objects.filter(
        empresa=request.user.extras.empresa
    ).order_by("nome")
    return render(request, "filiais.html", {"filiais": filiais_qs})


@login_required
def apagar_filial(request, filial_id):
    filial = get_object_or_404(Filial, id=filial_id, empresa=request.user.extras.empresa)
    if request.method == "POST":
        filial.delete()
    return redirect("filiais")
