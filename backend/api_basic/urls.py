from django.urls import path
from .views import players_list, entity_state, block_state, kill_state, last_kill, add_kill, all_entity_state, kill_stats

urlpatterns = [
    path('players/', players_list),
    path('entitystats/<slug:uid>', entity_state),
    path('blockstats/<slug:uid>', block_state),
    path('kills/<slug:met>/<slug:uid>', kill_state),
    path('kills/add', add_kill),
    path('kills/', kill_stats),
    path('lastkills/', last_kill),
    path('stats/', all_entity_state)
]