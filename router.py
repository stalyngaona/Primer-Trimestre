import network

# Configuración del punto de acceso
SSID = "Stalyn Gaona"
PASSWORD = "Stalyn01"

ap = network.WLAN(network.AP_IF)
ap.active(True)

# Configurar SSID, contraseña y modo de autenticación
ap.config(essid=SSID, password=PASSWORD, authmode=network.AUTH_WPA_WPA2_PSK)

# Opcional: asignar IP fija al AP
ap.ifconfig(("192.168.4.1", "255.255.255.0", "192.168.4.1", "8.8.8.8"))

print("Punto de acceso activado")
print("SSID:", SSID)
print("Contraseña:", PASSWORD)
print("IP del AP:", ap.ifconfig()[0])