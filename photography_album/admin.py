from django.contrib import admin
from .models import Photographs

@admin.register(Photographs)
class PhotographModel(admin.ModelAdmin):
    list_display = ("photograph_id", "title", "description")