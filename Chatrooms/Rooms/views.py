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
    return render(request,'Rooms/home.html')


def room(request):
    context = {'rooms':rooms}
    return render(request, 'Rooms/room.html',context)
