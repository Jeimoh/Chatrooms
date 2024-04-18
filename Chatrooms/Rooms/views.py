from django.shortcuts import render
from django.http import HttpResponse 



# Create your views here.

rooms = [
    {'id': 5, 'name': 'Dangerous Django'},
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'React learning'},
    {'id': 3, 'name': 'Django tricks for begginers'},
    {'id': 4, 'name': 'Learn Figma Design'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request,'Rooms/home.html',context)


def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    
    return render(request, 'Rooms/room.html',context)
