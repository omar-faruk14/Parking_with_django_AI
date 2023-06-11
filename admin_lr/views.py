from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegistrationForm, AdminRegistrationForm
from django.urls import reverse
from web_parking_app1.models import ParkingLot
def test(request):
    return HttpResponse("Hello login page test")

@login_required(login_url='user_login')
def user_dashboard(request):
    user = request.user
    parking_lots_user = ParkingLot.objects.all()
    return render(request, 'user_page/user_parking_information.html', {'user': user,'parking_lots_user':parking_lots_user})

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_admin)
def admin_dashboard(request):
    parking_lots = ParkingLot.objects.all()
    user = request.user
    return render(request, 'login_Registrition/admin_dashboard.html', {'user': user,'parking_lots':parking_lots})

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
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
            return redirect('user_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login_Registrition/login_user.html', {'form': form})

def login_admin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login_Registrition/login_admin.html', {'form': form})

@login_required(login_url='user_login')
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='admin_login')
def logout_admin(request):
    logout(request)
    return redirect('admin_login')

