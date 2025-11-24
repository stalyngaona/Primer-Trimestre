import time
import dht
from machine import Pin

# Configurar el sensor DHT11
sensor = dht.DHT11(Pin(14))   # Puedes cambiar el pin si usas otro

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        print("Temperatura:", temp, "°C")
        print("Humedad:", hum, "%")
        print("-----------------------")

    except Exception as e:
        print("Error al leer el sensor:", e)

    time.sleep(2)  # Leer cada 2 segundos