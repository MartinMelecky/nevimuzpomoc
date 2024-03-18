from django.contrib import admin

# Register your models here.
from .models import Kniha, Vers

admin.site.register(Kniha)
admin.site.register(Vers)