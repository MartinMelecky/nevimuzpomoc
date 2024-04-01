from django.shortcuts import render, redirect
from .models import Verse
# Create your views here.
from .models import *
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "Biblecz/index.html", {
        "kniha": Kniha.objects.all()
    })
def kapitola(request, kapitola_id):
    o = Kapitola.objects.get(pk=kapitola_id)
    return render(request, "Biblecz/oddeleni.html", {
          "od": o,
    })
def verse(request, verse_id):
    p = Verse.objects.get(pk=verse_id)
    return render(request, "Biblecz/pacienti.html", {
          "pa": p,
    })