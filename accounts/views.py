from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("/")
        messages.error(request, "Unsuccessful Registration. Invalid Information")
    form = NewUserForm()
    return render(request, 'register.html', {"register_form": form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')
            user = authenticate(username=username, password=psw)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    form = AuthenticationForm()
    return render(request, 'login.html', {"login_form": form})


def logout(request):
    logout(request)
    messages.info(request, "you have Successfully Logged Out")
    return redirect('/')
