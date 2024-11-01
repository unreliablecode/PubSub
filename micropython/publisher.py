from umqtt.simple import MQTTClient
import network
import time

#  Set your WiFi credentials
ssid = 'Wokwi-GUEST'
password = ''

# Set your MQTT server details
mqtt_server = '109.110.188.37'
client_id = 'micropython_client'

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print('Connected to WiFi')

# Create an MQTT client
client = MQTTClient(client_id, mqtt_server, user='unreliablecode', password='250304')
client.connect()
print('Connected to MQTT broker')

while True:
    message = b'Hello from micropython!'
    client.publish('topic/test', message)  # Publish to the same topic
    print('Message published')
    time.sleep(5)
