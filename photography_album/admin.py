from django.contrib import admin
from .models import Photographs, Albums

@admin.register(Photographs)
class PhotographModel(admin.ModelAdmin):
    list_display = ("photograph_id", "title", "description", "uploaded_by", "upload_date")

@admin.register(Albums)
class AlbumModel(admin.ModelAdmin):
    list_display = ("album_id", "name", "description", "created_by", "created_date")