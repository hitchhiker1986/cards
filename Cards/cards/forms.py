from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('german_sentence', 'hungarian_sentence')
        labels = {
            'german_sentence' : "Német mondat / Satz auf Deutsch",
            'hungarian_sentence': "Magyar mondat / Satz auf Ungarisch",
        }



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password')

        widgets = {
            'password': forms.PasswordInput()
        }


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

