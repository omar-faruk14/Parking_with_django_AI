from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm
from django.contrib.auth import login
from .forms import AdminLoginForm
from web_parking_app1.models import ParkingLot


def dashboard(request):
    username = request.user.username
    parking_lots = ParkingLot.objects.all()
    return render(request, 'carreview.html', {'username': username,'parking_lots': parking_lots})
def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = AdminRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_admin(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page after successful login
    else:
        form = AdminLoginForm()
    return render(request, 'login.html', {'form': form})
