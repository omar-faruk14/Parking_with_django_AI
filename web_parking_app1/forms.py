from django import forms
from .models import ParkingLot

class ParkingLotForm(forms.ModelForm):
    class Meta:
        model = ParkingLot
        fields = ['name', 'number_of_parking', 'parking_limit']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'number_of_parking': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Parking'}),
            'parking_limit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Parking Limit'}),
        }


