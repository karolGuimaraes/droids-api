from django.urls import path
from . import views

urlpatterns = [
    path('demandas', views.listar_demandas, name='listar_demandas'),
    path('demanda/<int:id>', views.buscar_demanda, name='buscar_demanda'),
    path('adicionar', views.adicionar_demanda, name='adicionar_demanda'),
    path('editar', views.editar_demanda, name='editar_demanda'),
    path('excluir/<int:id>', views.excluir_demanda, name='excluir_demanda'),
    path('finalizar/<int:id>', views.finalizar_demanda, name='finalizar_demanda'),

    path('usuario', views.criar_usuario, name='criar_usuario'),
]