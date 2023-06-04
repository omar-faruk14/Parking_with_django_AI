from django.shortcuts import render
from .models import ParkingLot


def home(request):
    parking_lots=ParkingLot.objects.all()
    return render(request,"carreview.html",{'parking_lots':parking_lots})