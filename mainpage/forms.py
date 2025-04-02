from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FeedBack,Client
from django.utils import timezone

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['project', 'client', 'feedback_text']

class ClientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=255,
        label='Имя',
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        max_length=32,
        label='Фамилия',
        widget=forms.TextInput(attrs={'placeholder': 'Фамилия'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    phone = forms.CharField(
        max_length=15,
        label='Телефон',
        widget=forms.TextInput(attrs={'placeholder': 'Телефон'})
    )

    class Meta(UserCreationForm.Meta):
        # model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email') # Добавляем поля к стандартным полям UserCreationForm

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False) # Сохраняем User, но пока не коммитим в базу
        user.first_name = self.cleaned_data['first_name'] # Заполняем имя пользователя (не путать с именем клиента)
        user.last_name = self.cleaned_data['last_name'] # Заполняем фамилию пользователя
        user.email = self.cleaned_data['email'] # Заполняем email пользователя
        user.last_login = timezone.now()
        if commit:

            user.save()
            client = Client.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                phone=self.cleaned_data['phone']
            )
            return client

        return user

