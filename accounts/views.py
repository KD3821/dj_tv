from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import LoginForm, RegistrationForm, UserUpdateForm, ContactForm
from django.contrib import messages

User = get_user_model()

def register_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        messages.success(request, 'Пользователь добавлен в систему.')
        return render(request, 'register_done.html', {'new_user': new_user})
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def update_view(request):
    contact_form = ContactForm()
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserUpdateForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.city = data['city']
                user.hotel = data['hotel']
                user.save()
                messages.success(request, 'Данные сохранены.')
                return render(request, 'update_done.html', {'user': user})
            return render(request, 'update.html', {'form': form, 'contact_form': contact_form})
        form = UserUpdateForm(initial={'city': user.city, 'hotel': user.hotel})
        return render(request, 'update_done.html', {'user': user})
    else:
        return redirect('accounts:login')


def delete_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            qs = User.objects.get(pk=user.pk)
            qs.delete()
            messages.error(request, 'Пользователь удален из системы.')
        return redirect('home')

def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            city = data['city']
            hotel = data['hotel']
            email = data['email']
            data = [{'city': city, 'email': email, 'hotel': hotel}]
            messages.success(request, 'Данные сохранены для администрации.')
            return redirect('accounts:update')
        else:
            return redirect('accounts:update')
    else:
        return redirect('accounts:login')