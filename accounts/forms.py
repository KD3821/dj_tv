
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from billing.models import City, Hotel

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Пароль не верный!')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Данный аккаунт отключен')
        return super(LoginForm, self).clean(*args, **kwargs)


class RegistrationForm(forms.ModelForm):
    email = forms.CharField(label="Введите email",
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Введите пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Введите пароль еще раз",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return data['password2']


class UserUpdateForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), required=True,
        widget=forms.Select(attrs={'class': 'form-control'}), label="Город"
    )
    hotel = forms.ModelChoiceField(
        queryset=Hotel.objects.all(), required=True,
        widget=forms.Select(attrs={'class': 'form-control'}), label="Отель"
    )

    class Meta:
        model = User
        fields = ('city', 'language')


class ContactForm(forms.Form):
    city = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Город"
    )
    hotel = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Отель"
    )
    email = forms.EmailField(
        required=True,  widget=forms.EmailInput(attrs={'class': 'form-control'}), label="Введите email"
    )

    class Meta:
        model = User
        fields = ('city', 'hotel')