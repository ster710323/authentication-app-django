from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from .forms import SignUpForm, EditProfileForm, ChangePasswordForm

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

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered')
            return redirect('index')
    else:
        form = SignUpForm()

    context = {'form': form,}
    return render(request, 'account/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'You have hanged your profile data.')
                return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form,}
    return render(request, 'account/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have hanged your password.')
            return redirect('index')
    else:
        form = ChangePasswordForm(user=request.user)

    context = {'form': form,}
    return render(request, 'account/change_password.html', context)