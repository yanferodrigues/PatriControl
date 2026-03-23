from django.shortcuts import render

def investimentos(request):
    return render(request, "investimentos.html")

def novo_investimento(request):
    return render(request, "novo investimento.html")
