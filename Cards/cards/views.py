from django.shortcuts import render
from .models import Card
import random
# Create your views here.


def show_card(request):
    cards = list(Card.objects.all())
    card = random.choice(cards)

    return render(request, 'show_card.html', {'card': card})
