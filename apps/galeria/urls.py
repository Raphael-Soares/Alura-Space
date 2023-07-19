from django.urls import path, include
from apps.galeria.views import index, imagem,buscar,nova_imagem, deletar_imagem



urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('deletar-imagem/', deletar_imagem, name='deletar_imagem'),
    path('nova-imagem/', nova_imagem, name='nova_imagem'),
  
]
