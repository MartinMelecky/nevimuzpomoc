from django.db import models

# Create your models here.
class Kniha(models.Model):
    nazevknihy = models.CharField(max_length=60)
    zkratkaknihy = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nazevknihy}, ({self.zkratkaknihy})"

class Kapitola(models.Model):
    cislokapitoly = models.IntegerField()
    kniha = models.ForeignKey(Kniha, on_delete = models.CASCADE, related_name="kapitoly")

    def __str__(self):
        return f"{self.cislokapitoly}" 
    
class Vers(models.Model):
    obsahverse = models.CharField(max_length = 1000)
    cisloverse = models.IntegerField()
    kapitola = models.ForeignKey(Kapitola, on_delete = models.CASCADE, related_name = "verse")

    def __str__(self):
        return f"{self.cisloverse} {self.obsahverse}"
