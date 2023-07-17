from django.urls import path
from django.views.generic import TemplateView

from .views import (
    UploadView,
    AlbumView,
    PhotographDetails
)

urlpatterns = [
    path('upload', UploadView.as_view(), name='upload_photograph'),
    path('albums', AlbumView.as_view(), name='albums'),
   # path('', TemplateView.as_view(template_name="registration/logout_success.html"), name='logout_success')
]