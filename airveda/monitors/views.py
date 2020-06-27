from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DeviceSerializer, HumidityReadingSerializer, TempratureReadingSerializer
from .models import Device, HumidityReading, TempratureReading

# Create your views here.


class DeviceView(APIView):

    def get(self, request, uid=None, parameter=None):

        if parameter is not None and uid is not None:   # Case: If requested for reading
            start_on = request.query_params.get('start_on', None)
            end_on = request.query_params.get('end_on', None)
            if start_on is not None and end_on is not None: # Check start and end time is provided
               
                if parameter.lower() == 'temperature':
                    data = TempratureReading.objects.filter( deviceId = uid, readingDateTime__range = [start_on, end_on])
                    serializer = TempratureReadingSerializer(data, many = True)
                    return Response(serializer.data)
                elif parameter.lower() == 'humidity':
                    data = HumidityReading.objects.filter( deviceId = uid, readingDateTime__range = [start_on, end_on])
                    serializer = HumidityReadingSerializer(data, many = True)
                    return Response(serializer.data)
                else:
                    return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
    
            else:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)

        elif uid is not None: # Case: If a specific device is requested
            try:
                queryset = Device.objects.get(uid=uid)
                serializer = DeviceSerializer(queryset)
            except Device.DoesNotExist:
                return Response("UID does't exist", status=status.HTTP_404_NOT_FOUND)
        else: # Case: If list of all devices is requested
            queryset = Device.objects.all()
            serializer = DeviceSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):
        if request.data.get('uid') and request.data.get('name'):
            serializer = DeviceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, uid):
        try:
            device = Device.objects.get(uid=uid)
            device.delete()
            return Response("Device and all it's readings deleted", status=status.HTTP_200_OK)
        except Device.DoesNotExist:
            return Response("UID does't exist", status=status.HTTP_404_NOT_FOUND)

