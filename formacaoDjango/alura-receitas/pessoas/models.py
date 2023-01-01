from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        """
        Apresenta na tela do administrador do site o nome digitado do usuário ao invés de "Pessoa object(1)
        :return:
        """
        return self.nome

