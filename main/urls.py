from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    homepage,
    test_page
)
from photography_album.views import PhotographDetails

urlpatterns = [
    path('', homepage, name='home'),
    path('about', TemplateView.as_view(template_name="main/about.html"), name='about'),
    path('test', test_page, name='test'),
    path('manage/', include('photography_album.urls')),
    path('photograph/<photograph_id>', PhotographDetails.as_view(), name='photograph_details')
   # path('', TemplateView.as_view(template_name="registration/logout_success.html"), name='logout_success')
]
