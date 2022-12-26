from django.shortcuts import render


def index(request):

    receitas = {
        1: 'Receita1',
        2: 'Receita2',
        3: 'Receita3'
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'index.html', dados)


def receita(request):
    return render(request, 'receita.html')
