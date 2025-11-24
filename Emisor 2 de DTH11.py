import network
import socket
import time
import dht
from machine import Pin

# Conectarse al Access Point
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Stalyn Gaona", "Stalyn01")

print("Conectando al Access Point...")
while not wlan.isconnected():
    time.sleep(0.5)

print("Conectado. IP:", wlan.ifconfig()[0])

# Sensor DHT11 o DHT22
d = dht.DHT11(Pin(14))   # Cambiar a DHT22 si lo usas

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()

        mensaje = f"sensor2:{temp},{hum}"

        print("Enviando datos...")
        sock.sendto(mensaje.encode(), ("192.168.4.1", 5005))

        print("Enviado:", mensaje)

    except Exception as e:
        print("Error enviando:", e)

    time.sleep(3)
