from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Room
class HomeView(View):
    def get(self, request):
        rooms = Room.objects.all()
        print(rooms)
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