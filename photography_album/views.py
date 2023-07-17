from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UploadPhotograph, AlbumForm
from .models import Photographs
from django.urls import reverse_lazy

class PhotographDetails(LoginRequiredMixin, View):
    def get(self, request, photograph_id):
        photograph = get_object_or_404(Photographs, photograph_id=photograph_id)

        context = {
            'photograph': photograph
        }
        return render(request, 'photographs_albums/photograph_details.html', context)

class PhotographView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadPhotograph
        photographs = Photographs.objects.filter(uploaded_by=request.user.id)

        context = {
            'form': form,
            'photographs': photographs,
        }
        return render(request, 'photographs_albums/photographs.html', context)

    def post(self, request):
        photograph_form = UploadPhotograph(
            request.POST, request.FILES
        )
        photograph_form.instance.uploaded_by = self.request.user

        if photograph_form.is_valid():
            messages.success(request, "Your photograph has been uploaded.")
            photograph_form.save()
            return redirect('photographs')
        else:
            messages.error(request, "There was an error uploading your photograph. Please try again.")
            return redirect('photographs')

class AlbumView(LoginRequiredMixin, View):
    def get(self, request):
        form = AlbumForm
        context = {"form": form}
        return render(request, "photographs_albums/albums.html", context)

    def post(self, request):
        album_form = AlbumForm(
            request.POST
        )
        album_form.instance.created_by = self.request.user
        if album_form.is_valid():
            messages.success(request, "Album created.")
            album_form.save()
            return redirect('albums')
        else:
            messages.error(request, "There was an error creating your album.")
            return redirect('albums')