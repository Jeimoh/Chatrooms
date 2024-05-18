from django.forms import ModelForm
from .models import Room,Message

class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields ='__all__'
class CreateMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
    