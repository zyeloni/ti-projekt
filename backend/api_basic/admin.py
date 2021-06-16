from django.contrib import admin
from .models import Players, EntityStats, BlockStats, KillStats


admin.site.register(Players)
admin.site.register(EntityStats)
admin.site.register(BlockStats)
admin.site.register(KillStats)
