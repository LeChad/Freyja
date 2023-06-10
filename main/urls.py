from django.urls import path
from django.views.generic import TemplateView
from .views import (
    homepage
)

urlpatterns = [
    path('', homepage, name='home'),

   # path('', TemplateView.as_view(template_name="registration/logout_success.html"), name='logout_success')
]
