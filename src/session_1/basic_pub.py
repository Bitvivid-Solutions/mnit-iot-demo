from src.libs.paho_client import PahoIoTClient


def default_pub_callback(client, userdata, mid):
    print("message was sent successfully")


class PahoPublisher(PahoIoTClient):
    def __init__(self, broker, port=1883, keepalive=60, callback=default_pub_callback):
        PahoIoTClient.__init__(self, broker, port, keepalive)
        self.paho_client.on_publish = callback

    def publish_message(self, topic, payload="test"):
        self.paho_client.publish(topic, payload)
