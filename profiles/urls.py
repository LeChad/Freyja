from django.urls import path
from django.views.generic import TemplateView
from .views import (
    MyProfile,
    UserProfile,
)

urlpatterns = [
    path('', MyProfile.as_view(), name='my_profile'),
    path('<username>', UserProfile.as_view(), name='user_profile'),
]
