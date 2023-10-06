from django.contrib import admin
from .models import Stand

@admin.register(Stand)
class StandAdmin (admin.ModelAdmin):
    list_display = ('localizacao','valor',)