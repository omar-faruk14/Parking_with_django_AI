from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegistrationForm, AdminRegistrationForm
from django.urls import reverse
def test(request):
    return HttpResponse("Hello login page test")

@login_required(login_url='user_login')
def user_dashboard(request):
    user = request.user
    return render(request, 'login_Registrition/user_dashboard.html', {'user': user})

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_admin)
def admin_dashboard(request):
    user = request.user
    return render(request, 'login_Registrition/admin_dashboard.html', {'user': user})

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_Registrition/user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'login_Registrition/register_user.html', {'form': form})

def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login_Registrition/admin_login.html')
    else:
        form = AdminRegistrationForm()
    return render(request, 'login_Registrition/register_admin.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login_Registrition/user_dashboard.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login_Registrition/login_user.html', {'form': form})

def login_admin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('admin_dashboard'))
    else:
        form = AuthenticationForm()
    return render(request, 'login_Registrition/login_admin.html', {'form': form})

@login_required(login_url='login_Registrition/user_login')
def logout_user(request):
    logout(request)
    return redirect('login_Registrition/user_login')

@login_required(login_url='login_Registrition/admin_login')
def logout_admin(request):
    logout(request)
    return redirect('login_Registrition/admin_login')

