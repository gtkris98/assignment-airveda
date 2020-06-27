from django.urls import include, path
from rest_framework import routers
from .views import DeviceView

# router = routers.DefaultRouter()
# router.register(r'devices', views.DeviceViewSet)
urlpatterns = [
    path('devices/', DeviceView.as_view(), name= 'devices'),
    path('devices/<int:uid>', DeviceView.as_view(), name= 'devices'),
    path('devices/<int:uid>/readings/<str:parameter>/', DeviceView.as_view(), name= 'devices')

]