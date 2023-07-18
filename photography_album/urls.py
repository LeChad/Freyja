from django.urls import path
from django.views.generic import TemplateView

from .views import (
    AlbumView,
    PhotographView,
add_to_album
)

urlpatterns = [
    path('albums', AlbumView.as_view(), name='albums'),
    path('photographs', PhotographView.as_view(), name='photographs'),
    path('add-to-album/<uuid:photograph_id>/', add_to_album, name='add_to_album'),
]