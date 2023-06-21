from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserUpdateForm, ProfileUpdateForm
from django.views import View

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfile(LoginRequiredMixin, View):
    def get(self, request, username):
        user_details = get_object_or_404(User, username=username)
        print(f"USERNAME: {username}")

        context = {'user': user_details}
        return render(request, 'profiles/profile.html', context)


class EditProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'profiles/edit_profile.html', context)

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
            messages.error(request, 'Error updating your profile')

            return render(request, 'profiles/edit_profile.html', context)

class MyProfile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'profiles/profile.html')
