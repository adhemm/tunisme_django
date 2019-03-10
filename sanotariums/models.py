from django.db import models

# Create your models here.
class Présentation(models.Model):
    adresse = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    indications_thérapeutiques = models.TextField(blank=False, null=False)

    def __str__(self):
        # hadhi mech ttebadel 5ater lazem ikoun nom ta3 sanotarium :)
        return("{}".format(self.adresse))

    def __unicode__(self):
        pass


class Galerie(models.Model):
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        # hadhi mech ttebadel 5ater lazem ikoun nom ta3 sanotarium :)
        return("{}".format(self.image))

    def __unicode__(self):
        pass
        

class FicheCenter(models.Model):
    nom_de_la_source = models.CharField(max_length=100, blank=False, null=False)
    téléphone = models.CharField(max_length=20, blank=False, null=True)
    fax = models.CharField(max_length=20, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    Société_gérante = models.CharField(max_length=120, blank=False, null=True)
    ouverture = models.DateField(auto_now=True)


    def __str__(self):
        # hadhi mech ttebadel 5ater lazem ikoun nom ta3 sanotarium :)
        return("Fiche Center")

    def __unicode__(self):
        pass
        
class Hébergement(models.Model):
    hébergement = models.TextField(blank=False, null=True)

    def __str__(self):
        # hadhi mech ttebadel 5ater lazem ikoun nom ta3 sanotarium :)
        length = len(self.hébergement) 
        if(length == 0):
            return("Empty")
        elif(length < 50):
            return("{}".format(self.hébergement[0:length - 1]))
        else:
            return("{}".format(self.hébergement[0:(length-25)] + "....."))

    def __unicode__(self):
        pass
        