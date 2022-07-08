from django import forms
from .models import Hotel, Room, Plan, Film
from django.contrib.auth import get_user_model

User = get_user_model()



class EditForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('plan', 'film')

    def __init__(self, hotel_id, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['plan'].queryset = Plan.objects.all().filter(hotel_id=hotel_id)


class ChangeForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name',)

    def __init__(self, name, *args, **kwargs):
        super(ChangeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = Room.objects.all().filter(name=name)



