from django.db import models

# Create your models here.


class Responsable(models.Model):
    nom = models.CharField(max_length=30, blank=False, null=False)
    prénom = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    adresse = models.CharField(max_length=50, blank=False, null=False)
    mot_de_pass = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return(" {}  {}".format(self.prénom, self.nom))

    def __unicode__(self):
        pass

