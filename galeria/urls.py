from django.urls import path
from galeria.views import index, pokemon

urlpatterns = [
    path('', index, name ='index'),
    path('pokemon/<int:poke_id>', pokemon, name='pokemon')
]