from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name = "room"),

    path('room/r/createRoom', views.createRoom, name="createRoom"),
    path('room/<str:pk>/update', views.updateRoom, name = "updateRoom"),

     path('room/createMessage/<str:pk>', views.createMessage, name="createMessage"),


]