from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("kapitola<int:kapitola_id>", views.kapitola, name="kapitola"),
    path("verse<int:verse_id>", views.verse, name="verse")
]