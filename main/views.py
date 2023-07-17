from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import NewUserForm
from profiles.models import Profile
from photography_album.models import (
    Photographs,
)

def homepage(request):
    photographs = Photographs.objects.all()[:15]
    context = {"photographs": photographs}
    return render(request, 'main/index.html', context)


def photographers(request):
    photographers_obj = Profile.objects.all().order_by('user')
    return render(request, 'main/photographers.html', {"photographers": photographers_obj})


def test_page(request):
    context = {}
    if request.method == "POST":
        send_mail(
            subject="Welcome to Freyja!",
            message=f"""Hello, test!
            
            Welcome to Project Freyja! A album and photography web application made for NAU class PLD450.
            Your registered username is, test. Please feel free to explore the project and provide
            any feedback. 

            Best Regards, 
            Freyja Team
            
            """,
            from_email="project.pld450@gmail.com",
            recipient_list=["lechadify@gmail.com"]
        )
        messages.info(request, "Sent message?")
    return render(request, 'main/test_page.html', context)


def sign_up(request):
    context = {}
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            checkbox_value = request.POST.get("agreement_checkbox")
            if checkbox_value == "on":
                form.save()
                messages.success(request, "Your account has been created.")

                send_mail(
                    subject="Welcome to Freyja!",
                    message=f"""
                        Hello, {request.POST.get('first_name')}!
                        
                        Welcome to Project Freyja! A album and photography web application made for NAU class PLD450.
                        Your registered username is, {request.POST.get('username')}. Please feel free to explore the project and provide
                        any feedback. 
                        
                        Best Regards, 
                        Freyja Team
                    """,
                    from_email="project.pld450@gmail.com",
                    recipient_list=[request.POST.get("email")]

                )
                return redirect('login')
            else:
                messages.error(request, "To create an account, please agree to our terms and conditions.")

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)