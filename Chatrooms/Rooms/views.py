from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Room, Message
from .forms import CreateRoomForm,CreateMessageForm

# Create your views here.

rooms = Room.objects.all()
messages = Message.objects.all()

def home(request):
    context = {'rooms':rooms}
    return render(request,'Rooms/home.html',context)


def room(request,pk):
    room = Room.objects.get(id = pk )
    message = Message.objects.filter(room = room)
    context = {'room': room, 'messages':message}
    
    return render(request, 'Rooms/room.html',context)
def createRoom(request):
    form = CreateRoomForm()
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'Rooms/createRoom.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id = pk)
    form = CreateRoomForm(instance = room)
    if request.method == 'POST':
        form = CreateRoomForm(request.POST, instance = room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'Rooms/createRoom.html', context)

def createMessage(request,pk):
    room = Room.objects.get(id = pk)
    form = CreateMessageForm(instance = room)
    if request.method == 'POST':
        form = CreateMessageForm(request.POST,instance = room)
        if form.is_valid:
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'Rooms/createMessage.html', context)
