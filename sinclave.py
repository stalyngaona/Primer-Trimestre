import network

ap = network.WLAN(network.AP_IF)   # Modo Access Point
ap.active(True)                    # Activar AP

ap.config(essid="Stalyn Gaona", authmode=network.AUTH_OPEN)  
# authmode=AUTH_OPEN → red sin contraseña

print("Punto de acceso creado correctamente")
print("SSID:", ap.config('essid'))
print("IP:", ap.ifconfig()[0])