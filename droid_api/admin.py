from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Demanda


class DemandaAdmin(admin.ModelAdmin):
    readonly_fields = ['status_imagem']
    fields = ['status_imagem', 'peca', 'anunciante', 'endereco_entrega']

admin.site.register(Demanda, DemandaAdmin)
admin.site.unregister(Group)