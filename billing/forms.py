from django import forms
from .models import Hotel, Room, Plan, Film

class HomeForm(forms.Form):
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), required=False,  widget=forms.Select(attrs={'class': 'form-control'}), label="Отель")



class EditForm(forms.Form):
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}), label="Отель")
    room = forms.ModelChoiceField(queryset=Room.objects.all(), required=False,  widget=forms.Select(attrs={'class': 'form-control'}), label="Категория номера")
    plan = forms.ModelChoiceField(queryset=Plan.objects.all(), required=False,  widget=forms.Select(attrs={'class': 'form-control'}), label="Тариф вкличен")
    film = forms.ModelChoiceField(queryset=Film.objects.all(), required=False,  widget=forms.Select(attrs={'class': 'form-control'}), label="Фильм включен")
