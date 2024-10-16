from django.shortcuts import render
from .models import Card
import random
# Create your views here.


def show_card(request):
    cards = list(Card.objects.all())
    card = random.choice(cards)

    return render(request, 'show_card.html', {'card': card})

def create_card(request):
    form = SentenceCardForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            card = SentenceCard()
            card.german_sentence = request.POST.get('german_sentence')
            card.hungarian_sentence = request.POST.get('hungarian_sentence')
            card.did_not_knew_counter = 0
            card.i_knew_counter = 0
            card.save()

        return HttpResponseRedirect('/thanks')
        print(form.non_field_errors)
        print(form.non_form_errors)

    return render(request, 'create_card.html', {'form': form})

def card_response(request):
    return render(request, 'response.html')
