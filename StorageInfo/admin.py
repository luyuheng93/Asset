from django.contrib import admin
from StorageInfo import models

# Register your models here.
admin.site.register(models.Asset)
admin.site.register(models.StorageDevice)
admin.site.register(models.Manufacturer)
admin.site.register(models.SanSwitch)