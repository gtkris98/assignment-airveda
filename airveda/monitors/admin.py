from django.contrib import admin
from .models import Device, HumidityReading, TempratureReading 
# Register your models here.
admin.site.register(Device)
admin.site.register(HumidityReading)
admin.site.register(TempratureReading)