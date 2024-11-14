from venv import logger

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Card
from .forms import CardForm, RegistrationForm  # ez az import hianyzott
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import *
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return HttpResponseRedirect('home')
        else:
            messages.error(request, 'Logged in Fail')
            return HttpResponseRedirect('accounts/login')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return (render(request, 'registration/login.html'))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect('home')
        else:
            form = PasswordChangeForm(request.user, request.POST)
            #messages.error(request, 'Jelszóváltoztatás sikertelen')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/pwchange.html', {'form': form})


@login_required
def show_card(request):
    cards = list(Card.objects.filter(owner__username=request.user.username))
    card = random.choice(cards)

    return render(request, 'show_card.html', {'card': card})

@login_required
def create_card(request):
    form = CardForm(request.POST) #ez hibásan SentenceCardForm volt, de ilyen nincs a forms.py file-ban, ott CardForm -nak hivjak
    if request.method == 'POST':
        if form.is_valid():
            card = Card() #itt is SentenceCard() volt, ilyen nincs, a models.py fileban Card osztaly van
            card.german_sentence = request.POST.get('german_sentence')
            card.hungarian_sentence = request.POST.get('hungarian_sentence')
            card.did_not_knew_counter = 0
            card.i_knew_counter = 0
            card.owner = request.user
            card.save()

        return HttpResponseRedirect('/thanks')
        print(form.non_field_errors)
        print(form.non_form_errors)

    return render(request, 'create_card.html', {'form': form})

@login_required
def card_response(request):
    return render(request, 'thanks.html')


def sign_up(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'],)
            login(request, user)
            request.session['is_connected'] = True
            return HttpResponseRedirect('create_card')
        else:
            form= RegistrationForm()

    return render(request, 'registration/register.html', {"form": form})