
from django import forms
from . models import Musician
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MusicianForm(forms.ModelForm):
    class Meta: 
        model = Musician
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set help_text to empty strings to remove help text
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email']
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
