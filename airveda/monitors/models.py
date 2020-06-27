from django.db import models
from django.utils import timezone

# Create your models here.


class Device(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)


class TempratureReading(models.Model):
    deviceId = models.ForeignKey(Device, on_delete=models.CASCADE)
    reading = models.DecimalField(max_digits=5, decimal_places=2)
    readingDateTime = models.DateTimeField(default=timezone.now())


class HumidityReading(models.Model):
    deviceId = models.ForeignKey(Device, on_delete=models.CASCADE)
    reading = models.DecimalField(max_digits=5, decimal_places=2)
    readingDateTime = models.DateTimeField(default=timezone.now())