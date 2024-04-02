from django.shortcuts import render, redirect
from .models import Vers
# Create your views here.
from .models import *
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "Biblecz/index.html", {
        "kniha": Kniha.objects.all()
    })
def kniha(request, kniha_id):
    r = Kniha.objects.get(pk=kniha_id)
    return render(request, "Biblecz/kapitola.html", {
          "ra": r.kapitoly.all(),
    })


def Kapitoly(request, kapitola_id):
    vybraneverse = Kapitola.objects.get(pk=kapitola_id)
    return render(request, "Biblecz/verse.html", {
          "verse": vybraneverse.verse.all(),
    })
"""
def verse(request, verse_id):
    p = Vers.objects.get(pk=verse_id)
    return render(request, "Biblecz/verse.html", {
          "pa": p,
    })
"""
