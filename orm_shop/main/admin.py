from django.contrib import admin

from main import models

admin.site.register(models.Car)
admin.site.register(models.Client)
admin.site.register(models.Sale)
