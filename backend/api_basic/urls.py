from django.urls import path
from .views import players_list, entity_state

urlpatterns = [
    path('players/', players_list),
    path('entitystats/<slug:uid>', entity_state)
]