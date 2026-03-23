from django.shortcuts import render

def ativos(request):
    return render(request, "ativos.html")

def novo_ativo(request):
    return render(request, "novo patrimonio.html")

def descricao_ativo(request):
    return render(request, "descricao ativo.html")