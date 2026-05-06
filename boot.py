import network
import time

# --- Configuration ---
WIFI_SSID = "Pranav"
WIFI_PASSWORD = "pranav94"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        # Wait for connection with a 10-second timeout
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
            
    if wlan.isconnected():
        config = wlan.ifconfig()
        print("\n--- Connection Successful ---")
        print("IP Address: ", config[0])
        print("Subnet Mask:", config[1])
        print("Gateway:    ", config[2])
        print("-----------------------------\n")
    else:
        print("Connection Failed. Please check your SSID/Password.")

# Run the connection
connect_wifi()

