from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from datetime import date
from .models import Room, Booking

class HomeView(View):
    def get(self, request):
        rooms = Room.objects.all().order_by('id')
        return render(request, 'base.html', {'rooms': rooms})
class AddNewRoom(View):
    def get(self, request):
        return render(request, 'add-room-form.html')
    
    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('hasProjector') == 'true'

        if not name:
            messages.error(request, 'Room name cannot be empty.')
            return render(request, 'add-room-form.html')
        
        room_exists = Room.objects.filter(name=name).exists()
        if room_exists:
            messages.error(request, "A room with this name already exists.")
            return render(request, 'add-room-form.html')
        
        if int(capacity) > 0:
            Room.objects.create(name=name, capacity=capacity, projector_availability=projector)
            return redirect('home')
        else:
            messages.error(request, "Capacity must be greater than 0.")
            return render(request, 'add-room-form.html')

class DeleteRoom(View):
    def get(self, request, id):
        Room.objects.filter(id=id).delete()
        return redirect('home')
    
class ModifyRoom(View):
    def get(self, request, id):
        room = get_object_or_404(Room, id=id)
        return render(request, 'edit-room-form.html', {'room': room})
    
    def post(self, request, id):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('hasProjector') == 'true'
        room = get_object_or_404(Room, id=id)

        if not name:
            messages.error(request, 'Room name cannot be empty.')
            return render(request, 'edit-room-form.html', {'room': room})
        
        name_exists = Room.objects.filter(name=name).exclude(id=id).exists()
        if name_exists:
            messages.error(request, "Another room with this name already exists.")
            return render(request, 'edit-room-form.html', {'room': room})
        
        if int(capacity) > 0:
            Room.objects.filter(id=id).update(
                name=name,
                capacity=int(capacity),
                projector_availability=projector
            )
            return redirect('home')
        else:
            messages.error(request, "Capacity must be greater than 0.")
            return render(request, 'edit-room-form.html')

class BookingRoom(View):
    def get(self, request, id):
        room = get_object_or_404(Room, id=id)
        return render(request, 'booking-form.html', {'room': room})

    def post(self, request, id):
        room = get_object_or_404(Room, id=id)
        
        booking_date_str = request.POST.get('date')
        comment = request.POST.get('comment')

        if not booking_date_str:
            messages.error(request, "Please select a date.")
            return render(request, 'booking-form.html', {'room': room})
        
        booking_date = date.fromisoformat(booking_date_str)
        if booking_date < date.today():
            messages.error(request, "You cannot book a room for a past date!")
            return render(request, 'booking-form.html', {'room': room})
        
        is_already_booked = Booking.objects.filter(room=room, date=booking_date).exists()
        if is_already_booked:
            messages.error(request, f"The room '{room.name}' is already booked for this day.")
            return render(request, 'booking-form.html', {'room': room})
        
        Booking.objects.create(date=booking_date, room=room, comment=comment)
        return redirect('home')
    
class SearchRoom(View):
    def get(self, request):
        name = request.GET.get('name')
        capacity = request.GET.get('capacity')
        projector = request.GET.get('hasProjector') == 'true'

        rooms_match = Room.objects.all().order_by('id')

        if name:
            rooms_match = rooms_match.filter(name__icontains=name)

        if capacity:
            rooms_match = rooms_match.filter(capacity__gte=int(capacity))

        if projector:
            rooms_match = rooms_match.filter(projector_availability=True)

        return render(request, 'base.html', {'rooms': rooms_match})