from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        # The user is registering a new account
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/register.html',
                              {'error': "Username already in use"})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/register.html',
                          {'error': "Passwords do not match"})
    else:
        # User wants to enter info
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',
                          {'error': "Username or Password is incorrect."})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    # TODO need to route to home page
    # TODO don't forget to log out
    return render(request, 'accounts/logout.html')
