from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Chat, Message


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class ChatCreateForm(ModelForm):
    user_owner_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Chat
        fields = ['user_owner_id']


class MessageCreateForm(ModelForm):
    chat_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Message
        fields = ['message', 'chat_id']

        widgets = {
            "message": forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder' : 'Сообщение...'
            }
            )
        }