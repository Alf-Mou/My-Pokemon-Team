from django.shortcuts import render, get_object_or_404

from galeria.models import Pokemon

def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'galeria/index.html', {"pokemon_grupo": pokemons})

def pokemon(request, poke_id):
    pokemon = get_object_or_404(Pokemon, pk=poke_id)
    return render(request, 'galeria/pokemon.html', {"pokemon": pokemon})
