from django.urls import path
from django.views.generic import TemplateView
from .views import (
    homepage,
    test_page
)

urlpatterns = [
    path('', homepage, name='home'),
    path('test', test_page, name='test')
   # path('', TemplateView.as_view(template_name="registration/logout_success.html"), name='logout_success')
]
