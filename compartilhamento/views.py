from django.shortcuts import render

# Create your views here.


def home(request):

    contexto = {
        'setor': 'Compartilhamento',
    }
    return render(request, 'pages/home.html', context=contexto)


def conversor(request):
    return render(request, 'pages/utils.html')
