from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'full_name']
class AdminLoginForm(AuthenticationForm):
    pass
