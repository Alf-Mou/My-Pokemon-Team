from django.contrib import admin

from galeria.models import Pokemon

class ListandoPokemons(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)

admin.site.register(Pokemon, ListandoPokemons)


