from django.urls import path, include
from apps.usuarios.views import login,cadastro, logout
from apps.galeria.views import index



urlpatterns = [
    path("",index, name="index"),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),

  
]
