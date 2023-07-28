# sensor/urls.py
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_sensor_data, name='read_sensor_data'),
]
'''
# sensor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.sensor_data, name='sensor_data'),
]
