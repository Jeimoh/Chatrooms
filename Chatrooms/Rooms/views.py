from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import Room, Message
from .forms import CreateRoomForm,CreateMessageForm

# Create your views here.

rooms = Room.objects.all()
messages = Message.objects.all()

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username == username)
        except:
            return HttpResponse('User does not Exist')
        

        


    context = {}
    return render(request, 'Rooms/login_register.html', context)

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
    return render(request, 'Rooms/create.html', context)

def createMessage(request,pk):
    room = get_object_or_404(Room, id=pk)
    form = CreateMessageForm()
    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = room  # Set the room
            message.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'Rooms/create.html', context)
def deleteRoom(request,pk):
    room = get_object_or_404(Room,id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'object':room}
    return render(request, 'Rooms/delete.html', context)

def deleteMessage(request,pk):
    message = get_object_or_404(Message,id = pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context = {'object':'This Message'}
    return render(request, 'Rooms/delete.html', context)
