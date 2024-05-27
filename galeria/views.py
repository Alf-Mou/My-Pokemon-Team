from django.shortcuts import render

from galeria.models import Pokemon

def index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'galeria/index.html')

def pokemon(request):
    return render(request, 'galeria/pokemon.html')
