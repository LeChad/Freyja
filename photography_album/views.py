from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UploadPhotograph
from .models import Photographs

class UploadView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadPhotograph
        context = {'form': form}
        return render(request, 'photographs_albums/index.html', context)

    def post(self, request):
        photograph_form = UploadPhotograph(
            request.POST, request.FILES
        )
        photograph_form.instance.uploaded_by = self.request.user

        if photograph_form.is_valid():
            messages.success(request, "Your photograph has been uploaded.")
            photograph_form.save()
            return redirect('upload_photograph')
        else:
            messages.error(request, "There was an error uploading your photograph. Please try again.")
            return redirect('upload_photograph')