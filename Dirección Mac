import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

mac = wlan.config("mac")
dir_mac = ":".join(["%02x"% b for b in mac])

print ("MAC WiFi:", dir_mac)
