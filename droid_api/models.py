from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Conta(User):
    telefone = models.CharField(max_length=50, null=True)

class Peca(models.Model):
    descricao = models.CharField(max_length=255)

class Endereco(models.Model):
    cep = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

class Demanda(models.Model):
    finalizada = models.BooleanField(default=False)
    peca = models.ForeignKey('Peca', on_delete=models.CASCADE)
    anunciante = models.ForeignKey('Conta', on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey('Endereco', on_delete=models.PROTECT)

    def status_imagem(self):
        if not self.finalizada:
            return mark_safe("<img src='/static/img/baseline-highlight_off.svg' />")
        else:
            return mark_safe("<img src='/static/img/baseline-check_circle_outline.svg' />")

    status_imagem.short_description = 'Status'
