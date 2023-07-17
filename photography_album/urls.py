from django.urls import path
from django.views.generic import TemplateView

from .views import (
    AlbumView,
    PhotographView,
)

urlpatterns = [
    path('albums', AlbumView.as_view(), name='albums'),
    path('photographs', PhotographView.as_view(), name='photographs'),
]