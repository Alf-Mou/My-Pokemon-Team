from django.urls import path
from galeria.views import index, pokemon

urlpatterns = [
    path('', index, name ='index'),
    path('pokemon/', pokemon, name='pokemon')
]