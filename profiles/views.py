from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileUpdateForm, UserUpdateForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    User,
    Profile
)
from photography_album.models import (
    Photographs,
    Albums
)


class UserProfile(LoginRequiredMixin, View):
    def get(self, request, username):
        user_details = get_object_or_404(User, username=username)
        albums = Albums.objects.filter(created_by=user_details.id)
        photographs = Photographs.objects.filter(uploaded_by=user_details.id)

        context = {
            'user': user_details,
            'albums': albums,
            'photographs': photographs
        }
        return render(request, 'profiles/profile.html', context)


class EditProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'profiles/partials/_edit.html', context)

    def post(self, request):
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Your profile has been updated successfully')
            return redirect('my_profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request, 'Error updating you profile')
            return render(request, 'profiles/partials/_edit.html', context)


class MyProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_details = get_object_or_404(User, username=request.user.profile.user)
        albums = Albums.objects.filter(created_by=user_details.id)
        photographs = Photographs.objects.filter(uploaded_by=user_details.id)

        context = {
            'user': user_details,
            'albums': albums,
            'photographs': photographs
        }
        return render(request, 'profiles/profile.html', context)
