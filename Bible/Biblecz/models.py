from django.db import models

# Create your models here.
class Verse(models.Model):
    obsahverse = models.CharField(max_length = 60)
    cisloverse = models.IntegerField(max_length = 60)

    def __str__(self):
        return f"{self.cisloverse} {self.obsahverse} "    

class Kapitola(models.Model):
    cislokapitoly = models.IntegerField(max_length=60)
    vers = models.ForeignKey(Verse, on_delete = models.CASCADE, related_name = "Kapitola")

    def __str__(self):
        return f"{self.cislokapitoly} {self.vers}" 
    
class Kniha(models.Model):
    nazevknihy = models.CharField(max_length=60)
    zkratkaknihy = models.CharField(max_length=60)
    kapitola = models.ForeignKey(Kapitola, on_delete = models.CASCADE, related_name="Kniha")

    def __str__(self):
        return f"{self.nazevknihy}, ({self.zkratkaknihy}), ({self.kapitola})"
    