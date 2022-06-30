from django.shortcuts import render, redirect
from .models import Room, Hotel
from .forms import HomeForm, EditForm


def home_view(request):
    form = HomeForm()
    return render(request, 'home.html', {'form': form})

def list_view(request):
    form = HomeForm()
    hotel = request.GET.get('hotel')
    hotel_chosen = Hotel.objects.get(id=hotel)
    hotel_name = hotel_chosen.name
    hotel_city = hotel_chosen.city
    context = {'hotel': hotel, 'hotel_name': hotel_name, 'hotel_city': hotel_city, 'form': form}
    if hotel:
        qs = Room.objects.all().filter(hotel=hotel)
        context['object_list'] = qs
    return render(request, 'list.html', context)

def edit_view(request):
    form = EditForm()
    hotel = request.GET.get('hotel')
    room = request.GET.get('room')
    plan = request.GET.get('plan')
    film = request.GET.get('film')
    context = {'hotel': hotel, 'room': room, 'plan': plan, 'film': film, 'form': form}
    if request.method == 'POST':
        edit_form = EditForm(request.POST or None)
        if edit_form.is_valid():
            data = edit_form.cleaned_data
            room = data['room']
            plan = data['plan']
            film = data['film']
            # data = [{'hotel': hotel, 'room': room, 'plan': plan, 'film': film}]
            data.save()
            return redirect('list.html')
        else:
            return redirect('list.html')
    if hotel:
        qs = Room.objects.all().filter(hotel=hotel)
        context['object_list'] = qs
    return render(request, 'list.html', context)