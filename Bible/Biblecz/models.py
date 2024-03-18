from django.db import models

# Create your models here.
class Vers(models.Model):
    obsahverse = models.CharField(max_length=100,)
    cisloverse = models.IntegerField(max_length=60)

    def __str__(self):
        return f"{self.cisloverse} {self.obsahverse}"    

class Kniha(models.Model):
    nazev = models.CharField(max_length=64, )
    kapitola = models.IntegerField(max_length=60)
    verse = models.ForeignKey(Vers, on_delete = models.CASCADE, related_name="Kniha")

    def __str__(self):
        return f"{self.nazev} ({self.kapitola}) ({self.verse})"
    