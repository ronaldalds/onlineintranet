from django.shortcuts import render


# Create your views here.
def informacoes(request):
    return render(request, 'projeto-rede-informacoes.html')
