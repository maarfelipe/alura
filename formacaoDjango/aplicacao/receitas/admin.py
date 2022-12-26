from django.contrib import admin
from .models import Receita


class exibir_receita(admin.ModelAdmin):
    list_display = ('nome_receita',)


admin.site.register(Receita, exibir_receita)
