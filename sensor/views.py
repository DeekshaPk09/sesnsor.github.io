# sensor/views.py
'''
import time
import Adafruit_DHT
from django.shortcuts import render
from .models import SensorData

def read_sensor_data(request):
    # Read temperature and humidity from DHT11 sensor (GPIO pin 4)
    sensor = Adafruit_DHT.DHT11
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print(humidity)

    # Store data in the database using the SensorData model
    if humidity is not None and temperature is not None:
        data = SensorData.objects.create(temperature=temperature, humidity=humidity)
        data.save()
    else:
        # If the reading failed, display an error message
        return "Failed to retrieve data from the sensor."
     # Get the current time
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        # Wait for 60 seconds before reading data again
    time.sleep(60)

    return render(request, 'sensor_data.html', {'temperature': temperature, 'humidity': humidity, 'current_time': current_time})
'''
# sensor/views.py
'''
import time
import Adafruit_DHT
from django.shortcuts import render
from .models import SensorData
from datetime import datetime

def get_sensor_data(request):
    # GPIO pin and sensor type (DHT11 or DHT22)
    pin = 4
    sensor = Adafruit_DHT.DHT11

    # Read temperature and humidity from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Store data in the database using the SensorData model
    if humidity is not None and temperature is not None:
        data = SensorData.objects.create(temperature=temperature, humidity=humidity)
        data.save()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(1)

    # Return the current time and sensor data to the template
    from .models import SensorDatareturn render(request, 'sensor_data.html', {'temperature': temperature, 'humidity': humidity,'current_time': current_time})
'''
# In your Django views.py
'''
from django.http import JsonResponse
import Adafruit_DHT
import time

def get_temperature_humidity(request):
    # Replace with appropriate GPIO pin and sensor type (DHT11 or DHT22)
    sensor = Adafruit_DHT.DHT22
    pin = 4

    # Read data from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        data = {
            'temperature': '{0:0.1f}'.format(temperature),
            'humidity': '{0:0.1f}'.format(humidity)
        }
    else:
        data = {
            'error': 'Failed to retrieve data from the sensor.'
        }

    return JsonResponse(data)
'''
# In your Django views.py
'''
from django.shortcuts import render
import Adafruit_DHT

def sensor_data(request):
    # Replace with appropriate GPIO pin and sensor type (DHT11 or DHT22)
    sensor = Adafruit_DHT.DHT22
    pin = 4

    # Read data from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    context = {
        'temperature': '{0:0.1f}'.format(temperature) if temperature is not None else 'N/A',
        'humidity': '{0:0.1f}'.format(humidity) if humidity is not None else 'N/A',
    }

    return render(request, 'sensor_data.html', context)

'''
# In your Django views.py
# In your Django views.py
from django.shortcuts import render
import Adafruit_DHT

def sensor_data(request):
    sensor = Adafruit_DHT.DHT11
    pin = 4

    # Read data from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    context = {
        'temperature': temperature,
        'humidity': '{0:0.1f}'.format(humidity) ,
    }

    return render(request, 'sensor_data.html', context)


