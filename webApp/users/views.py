# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def profile(request):
    return render(request, "users/profile.html")


def signout(request):
    logout(request)

    return render(request, "users/register.html")

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            
            user = form.get_user()
            login(request,user)
            
            return redirect('/post/home/')
        print('inside if')    
        
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'form':form})
