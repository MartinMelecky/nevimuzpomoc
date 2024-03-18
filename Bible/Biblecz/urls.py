from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:kniha_id>", views.kniha, name="kniha"),
    path("<int:kniha_id>/vers", views.vers, name="vers"),
]