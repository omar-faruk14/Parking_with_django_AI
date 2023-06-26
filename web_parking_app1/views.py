from django.shortcuts import render, HttpResponse , redirect, get_object_or_404
from .models import ParkingLot
from .forms import ParkingLotForm
from .models import ParkingLot, VehicleEntry
from django.utils import timezone
from django.contrib import messages
#===================================Home page==========================================
def home(request):
    return render(request, 'user_page/home.html')

def user_parking_description(request):
    parking_lots_user=ParkingLot.objects.all()
    return render(request,"user_page/user_parking_information.html",{'parking_lots_user':parking_lots_user})

def add_parking_lot(request):
    if request.method == 'POST':
        form = ParkingLotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard') # Render a success page
    else:
        form = ParkingLotForm()

    return render(request, 'add_parking_lot.html', {'form': form})




def update_parking_lot(request, pk):
    parking_lot = get_object_or_404(ParkingLot, pk=pk)

    if request.method == 'POST':
        form = ParkingLotForm(request.POST, instance=parking_lot)
        if form.is_valid():
            form.save()
            # Redirect to the home page or display a success message
            return redirect('admin_dashboard')
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
        return redirect('admin_dashboard')  # Redirect to the home page after deletion
    return HttpResponse("Deletion is not completed")
#====================parking lot in out============================


def parking_lot_detail(request, parking_lot_id):
    parking_lot = get_object_or_404(ParkingLot, id=parking_lot_id)

    if request.method == 'POST':
        if 'in' in request.POST:
            vehicle_registration_Name = request.POST.get('vehicle_registration_Name')
            try:
                entry = VehicleEntry.objects.create(parking_lot=parking_lot, vehicle_registration_Name=vehicle_registration_Name)
                entry.save()
                parking_lot.number_of_parking += 1  # Increase the count of parking by 1
                parking_lot.save()
                messages.success(request, 'Vehicle successfully parked.')
            except Exception as e:
                messages.error(request, f'Failed to park vehicle: {str(e)}')
        elif 'out' in request.POST:
            entry_id = request.POST.get('entry_id')
            entry = parking_lot.vehicleentry_set.filter(vehicle_registration_Name=entry_id, exit_time__isnull=True).first()
            if entry:
                entry.exit_time = timezone.now()
                entry.save()
                parking_lot.number_of_parking -= 1  # Decrease the count of parking by 1
                parking_lot.save()
                messages.success(request, 'Vehicle successfully exited.')
            else:
                messages.error(request, 'Entry ID not found.')

    context = {
        'parking_lot': parking_lot
    }
    return render(request, 'parking_lot_in_out.html', context)






# def parking_lot_detail(request, parking_lot_id):
#     parking_lot = ParkingLot.objects.get(id=parking_lot_id)

#     if request.method == 'POST':
#         if 'in' in request.POST:
#             parking_lot.number_of_parking += 1
#             parking_lot.save()
#         elif 'out' in request.POST:
#             if parking_lot.number_of_parking > 0:
#                 parking_lot.number_of_parking -= 1
#                 parking_lot.save()

#     context = {
#         'parking_lot': parking_lot
#     }
#     return render(request, 'parking_lot_detail.html', context)



def map(request):
    return render(request, 'user_page/map.html')


#==================================**************************Command***************

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ParkingLot

@csrf_exempt
def update_parking_lot2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        action = data.get('action')

        try:
            parking_lot = ParkingLot.objects.get(name=name)
        except ParkingLot.DoesNotExist:
            return JsonResponse({'error': 'Parking lot not found'}, status=404)

        if action == 'in':
            parking_lot.number_of_parking += 1
            parking_lot.save()
        elif action == 'out':
            if parking_lot.number_of_parking == 0:
                return JsonResponse({'error': 'No available parking'}, status=400)
            parking_lot.number_of_parking -= 1
            parking_lot.save()
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

        return JsonResponse({'message': 'Parking lot updated successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
