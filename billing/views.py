from django.shortcuts import render, redirect, reverse
from .models import Room, Hotel, Plan
from .forms import EditForm, ChangeForm
from django.forms import modelformset_factory


def home_view(request):
    user = request.user
    if user.is_authenticated:
        hotel_id = user.hotel_id
        hotel = Hotel.objects.get(id=hotel_id)
        hotel_name = hotel.name
        hotel_city = hotel.city
        qs = Room.objects.all().filter(hotel_id=hotel_id)
        context = {'user': user, 'hotel_id': hotel_id, 'hotel_name': hotel_name, 'hotel_city': hotel_city, 'object_list': qs}
        return render(request, 'home.html', context)
    else:
        return redirect('accounts:login')



def list_view(request):

    user = request.user
    hotel_id = user.hotel_id
    hotel = Hotel.objects.get(id=hotel_id)
    hotel_name = hotel.name
    hotel_city = hotel.city
    context = {'user': user, 'hotel_id': hotel_id, 'hotel_name': hotel_name, 'hotel_city': hotel_city}
    room_form_set = modelformset_factory(Room, fields=('name', 'plan', 'film', 'deposit'), extra=0)
    data = request.POST or None
    formset = room_form_set(data=data, queryset=Room.objects.filter(hotel_id=hotel_id))
    for form in formset:
        form.fields['plan'].queryset = Plan.objects.all().filter(hotel_id=hotel_id)
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('home')
    else:
        context['formset'] = formset
        return render(request, 'list.html', context)




def edit_view(request):
    edit_form = EditForm(request.POST or None)
    user = request.user
    hotel_id = user.hotel_id
    hotel = Hotel.objects.get(id=hotel_id)
    qs = Room.objects.all().filter(hotel_id=hotel_id)
    hotel_name = hotel.name
    hotel_city = hotel.city
    context = {'hotel_name': hotel_name, 'hotel_city': hotel_city, 'qs': qs}
    if request.method == 'POST':
        if edit_form.is_valid():
            data = edit_form.cleaned_data
            plan = data['plan']
            film = data['film']
            context['object_list'] = qs
            return render(request, 'list.html', context)
        else:
            return render(request, 'edit.html', {'form': edit_form})
    else:
        form = EditForm(instance=hotel)
        context ['form'] = form
        return render(request, 'edit.html', context)
