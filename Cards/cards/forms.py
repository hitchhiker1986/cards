from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('german_sentence', 'hungarian_sentence')
        labels = {
            'german_sentence' : "Német mondat / Satz auf Deutsch",
            'hungarian_sentence': "Magyar mondat / Satz auf Ungarisch",
        }
