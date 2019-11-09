from src.libs.paho_client import PahoIoTClient
import time

def default_sub_callback(client, userdata, msg):
    if msg is not None:
        print(f"Received {msg.payload} on topic: {msg.topic}")


class PahoSubscriber(PahoIoTClient):
    def __init__(self, broker, port=1883, keepalive=60, callback=default_sub_callback):
        PahoIoTClient.__init__(self, broker, port, keepalive)
        self.paho_client.on_message = callback

    def subscribe_topic(self, topic, loop_timeout=10, qos=0):
        self.paho_client.subscribe(topic, qos)
        print("subscribed to: ", topic)
        self.paho_client.loop_start()
        start_time = time.time()
        while time.time() <= start_time + loop_timeout:
            time.sleep(1)
        self.paho_client.loop_stop()