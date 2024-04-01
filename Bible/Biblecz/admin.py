from django.contrib import admin

# Register your models here.
from .models import Kniha, Verse, Kapitola

admin.site.register(Kniha)
admin.site.register(Kapitola)
admin.site.register(Verse)