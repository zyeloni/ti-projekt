from django.urls import path
from .views import players_list, entity_state, block_state

urlpatterns = [
    path('players/', players_list),
    path('entitystats/<slug:uid>', entity_state),
    path('blockstats/<slug:uid>', block_state)
]