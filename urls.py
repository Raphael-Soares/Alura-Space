from django.urls import path, include
from galeria.views import index, imagem,buscar



urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar')
  
]
