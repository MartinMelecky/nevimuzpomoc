from django.shortcuts import render, redirect
from .models import Vers
# Create your views here.
from .models import Kniha
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "Biblecz/index.html", {
        "Bibelcz": Kniha.objects.all()
    })
def kniha(request, kniha_id):
    k = Kniha.objects.get(pk=kniha_id)
    return render(request, "Biblecz/verse.html", {
          "kniha": k,
          "vers": Kniha.verse.first(),
          "non_passengers": Vers.objects.exclude(k=kniha).all()
    })


def vers(request, kniha_id):
    if request.method == "POST":
        kniha = Kniha.objects.get(pk=kniha_id)
        passenger = Vers.objects.get(pk=int(request.POST["vers"]))
        passenger.kniha.add(kniha)
        return redirect(f'Biblecz/{kniha_id[0]}')