from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("kapitola<int:kapitola_id>", views.oddeleni, name="kapitola"),
    path("verse<int:verse_id>", views.pacienti, name="verse")
]