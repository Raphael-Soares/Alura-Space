from django.shortcuts import get_object_or_404, render, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages

from apps.galeria.forms import FotografiaForms




def index(request):
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)


    if not request.user.is_authenticated:

        messages.error(request,"Voce deve estar logado para acessar esta página" )
        return redirect("login")

    return render(
        request, 'galeria/index.html', {"cards": fotografias}
    )

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    if not request.user.is_authenticated:

        messages.error(request,"Voce deve estar logado para acessar esta página" )
        return redirect("login")


    return render(
        request, 'galeria/imagem.html', {"fotografia": fotografia}
    )

def buscar(request):
    if not request.user.is_authenticated:

        messages.error(request,"Voce deve estar logado para acessar esta página" )
        return redirect("login")

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    
    return render(
        request, 'galeria/buscar.html', {"cards": fotografias}
    )


def nova_imagem(request):

    if not request.user.is_authenticated:

        messages.error(request,"Voce deve estar logado para acessar esta página" )
        return redirect("login")
    

    form = FotografiaForms
    if request.method == "POST":
        form = FotografiaForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nova fotografia cadastrada")
            return redirect("index")
            

    return render(request, 'galeria/nova_imagem.html', {'form':form})


def deletar_imagem(request):
    if not request.user.is_authenticated:

        messages.error(request,"Voce deve estar logado para acessar esta página" )
        return redirect("login")

    return render(request)

