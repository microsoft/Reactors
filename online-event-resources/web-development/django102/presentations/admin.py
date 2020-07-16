from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Presentation)
admin.site.register(models.Speaker)
admin.site.register(models.Track)

