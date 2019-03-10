from django.contrib import admin

from .models import Responsable

admin.site.register(Responsable)



class MyAdminSite(admin.AdminSite):
    index_template = 'myadmin/index.html'
    login_template = 'myadmin/login.html'
    logout_template = 'myadmin/login.html'
    app_index_template = 'myadmin/index.html'


myadmin = MyAdminSite(name="myadmin")
