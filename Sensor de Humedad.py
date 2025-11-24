from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(23))

while True:
    try:
        sleep(1)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp*(9/5) + 32.0
        print('Temperature:%3.1fC'%temp)
        print('Temperature:%3.1F'%temp_f)
        print('Humidity:%3.1fC'%hum)
    except OSError as e:
        print('Failed to read sensor.')
