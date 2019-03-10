from django.contrib import admin

from .models import Présentation, Hébergement, Galerie, FicheCenter

admin.site.register(Présentation)
admin.site.register(Hébergement)
admin.site.register(Galerie)
admin.site.register(FicheCenter)

# Register your models here.
