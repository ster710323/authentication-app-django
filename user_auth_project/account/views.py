from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'account/index.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You successfully logged in'))
            return redirect('index')
        else:
            messages.error(request, ('Error Logging in - Please try again'))
            return redirect('login')
    else:
        return render(request, 'account/login.html', {})

def Logout_user(request):
    logout(request)
    messages.success(request, "You have been Logout successfully")
    return redirect('index')
