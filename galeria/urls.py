from django.urls import path, include
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='home'),
    path('imagem/', imagem, name='imagem')
]
