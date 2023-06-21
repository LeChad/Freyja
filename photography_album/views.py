from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UploadPhotograph

class UploadView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadPhotograph
        context = {'form': form}
        return render(request, 'photographs_albums/index.html', context)

    def post(self, request):
        pass