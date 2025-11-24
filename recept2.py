import network
import socket
import time

# Configurar Access Point
SSID = "Stalyn Gaona"
PASSWORD = "Stalyn01"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD, authmode=network.AUTH_WPA_WPA2_PSK)

# IP fija del AP
ap.ifconfig(("192.168.4.1", "255.255.255.0", "192.168.4.1", "8.8.8.8"))

print("\nESP32 configurado como Access Point")
print("SSID:", SSID)
print("IP:", ap.ifconfig()[0])
print("\nEsperando datos...\n")

# Crear socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.4.1", 5005))

while True:
    try:
        data, addr = sock.recvfrom(1024)
        mensaje = data.decode()

        # ------------------------------
        # Sensor 1
        # ------------------------------
        if mensaje.startswith("sensor1:"):
            temp, hum = mensaje.replace("sensor1:", "").split(",")
            print(f"[Sensor 1]  Temp: {temp}°C | Hum: {hum}%   → desde {addr[0]}")

        # ------------------------------
        # Sensor 2
        # ------------------------------
        elif mensaje.startswith("sensor2:"):
            temp, hum = mensaje.replace("sensor2:", "").split(",")
            print(f"[Sensor 2]  Temp: {temp}°C | Hum: {hum}%   → desde {addr[0]}")

        # ------------------------------
        # Otros mensajes
        # ------------------------------
        else:
            print("Dato recibido:", mensaje)

    except Exception as e:
        print("Error al recibir:", e)
        time.sleep(1)