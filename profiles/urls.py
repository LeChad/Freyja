from django.urls import path
from django.views.generic import TemplateView
from .views import (
    MyProfile
)

urlpatterns = [
    path('', MyProfile.as_view(), name='my_profile'),
    #path('<username>', profile, name='user-profile'),
]
