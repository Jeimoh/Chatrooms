from django.shortcuts import render
from django.http import HttpResponse 
from .models import Room, Message


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
