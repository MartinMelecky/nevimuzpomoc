from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("kapitoly/<int:kapitola_id>", views.Kapitoly, name="kapitoly"),
    #path("verse/<int:verse_id>", views.verse, name="verse"),
    path("kniha/<int:kniha_id>", views.kniha, name="kniha"),
]