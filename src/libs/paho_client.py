import paho.mqtt.client as mqtt

# def connect_callback():
#     print()

class PahoIoTClient:
    def __init__(self, broker, port=1883, keepalive=60):
        self.paho_client = mqtt.Client()
        self.paho_client.connect(broker, port, keepalive)

    def get_paho_client(self):
        return self.paho_client

