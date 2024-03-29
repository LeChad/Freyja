from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UploadPhotograph, AlbumForm, AlbumContent
from .models import Photographs, Albums

class PhotographDetails(LoginRequiredMixin, View):
    def get(self, request, photograph_id):
        photograph = get_object_or_404(Photographs, photograph_id=photograph_id)

        context = {
            'photograph': photograph
        }
        return render(request, 'photographs_albums/photograph_details.html', context)


def add_to_album(request, photograph_id):
    if request.method == 'POST':
        form = AlbumContent(user=request.user, request=request, data=request.POST)
        if form.is_valid():
            album_content = form.save(commit=False)
            album_content.album_id_id = request.POST['albumSelection']
            album_content.photograph_id_id = photograph_id
            album_content.created_by = request.user
            album_content.save()
            messages.success(request, "Added photograph to album")
            return redirect('photographs')  # Redirect to a success page after saving the form
    else:
        form = AlbumContent(user=request.user, request=request)
    return redirect('photographs')


class PhotographView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadPhotograph
        albumSelection = AlbumContent(request.user)
        photographs = Photographs.objects.filter(uploaded_by=request.user.id)

        context = {
            'form': form,
            'photographs': photographs,
            'albumContent': albumSelection
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
        albums = Albums.objects.filter(created_by=request.user)

        context = {"form": form,
                   "albums": albums }
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