from rest_framework import serializers
from .models import Device, HumidityReading, TempratureReading


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('uid', 'name')

class TempratureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempratureReading
        fields = ('deviceId', 'reading', 'readingDateTime')

class HumidityReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityReading
        fields = ('deviceId', 'reading', 'readingDateTime')