from django.shortcuts import render,HttpResponse
from .models import ParkingLot
from .forms import ParkingLotForm

def home(request):
    parking_lots = ParkingLot.objects.all()

    for parking_lot in parking_lots:
        available_percentage = (parking_lot.number_of_parking / parking_lot.parking_limit) * 100
        parking_lot.available_percentage = round(available_percentage)

    return render(request, 'carreview.html', {'parking_lots': parking_lots})


from django.shortcuts import render
from .forms import ParkingLotForm

def add_parking_lot(request):
    if request.method == 'POST':
        form = ParkingLotForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request) # Render a success page
    else:
        form = ParkingLotForm()

    return render(request, 'add_parking_lot.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import ParkingLot
from .forms import ParkingLotForm

def update_parking_lot(request, pk):
    parking_lot = get_object_or_404(ParkingLot, pk=pk)

    if request.method == 'POST':
        form = ParkingLotForm(request.POST, instance=parking_lot)
        if form.is_valid():
            form.save()
            # Redirect to the home page or display a success message
            return home(request)
        else:
            # Display an error message or notification if the form is invalid
            error_message = 'Failed to update parking lot. Please check the form inputs.'
            return render(request, 'error.html', {'error_message': error_message})
    else:
        form = ParkingLotForm(instance=parking_lot)

    return render(request, 'edit_parking_lot.html', {'form': form, 'parking_lot': parking_lot})


def delete_parking_lot(request, parking_lot_id):
    parking_lot = ParkingLot.objects.get(id=parking_lot_id)
    if request.method == 'POST':
        parking_lot.delete()
        return redirect('home')  # Redirect to the home page after deletion
    return HttpResponse("Deletion is not completed")


def parking_lot_detail(request, parking_lot_id):
    parking_lot = ParkingLot.objects.get(id=parking_lot_id)

    if request.method == 'POST':
        if 'in' in request.POST:
            parking_lot.number_of_parking += 1
            parking_lot.save()
        elif 'out' in request.POST:
            if parking_lot.number_of_parking > 0:
                parking_lot.number_of_parking -= 1
                parking_lot.save()

    context = {
        'parking_lot': parking_lot
    }
    return render(request, 'parking_lot_detail.html', context)

