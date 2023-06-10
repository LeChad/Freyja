from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import NewUserForm

def homepage(request):
    context = {}
    return render(request, 'main/index.html', context)


def sign_up(request):
    context = {}
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            checkbox_value = request.POST.get("agreement_checkbox")
            if checkbox_value == "on":
                form.save()
                messages.success(request, f"Your account has been created.")
                return redirect('login')
            else:
                messages.error(request, "To create an account, please agree to our terms and conditions.")

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)