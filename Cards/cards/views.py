from django.shortcuts import render
from .models import Card
from .forms import CardForm # ez az import hianyzott
import random
# Create your views here.


def show_card(request):
    cards = list(Card.objects.all())
    card = random.choice(cards)

    return render(request, 'show_card.html', {'card': card})

def create_card(request):
    form = CardForm(request.POST) #ez hibásan SentenceCardForm volt, de ilyen nincs a forms.py file-ban, ott CardForm -nak hivjak
    if request.method == 'POST':
        if form.is_valid():
            card = Card() #itt is SentenceCard() volt, ilyen nincs, a models.py fileban Card osztaly van
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
    pass
    #return render(request, 'response.html')
