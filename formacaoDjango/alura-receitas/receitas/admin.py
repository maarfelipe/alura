from django.contrib import admin
from .models import Receita


class ExibirReceita(admin.ModelAdmin):
    list_display = ('id', 'nome_receita')


admin.site.register(Receita, ExibirReceita)
