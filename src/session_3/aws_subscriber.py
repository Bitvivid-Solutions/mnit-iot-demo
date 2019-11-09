from src.libs.aws_client import AwsIoTClient

from src.libs import aws_client
import time

myMQTTClient = aws_client.get_client("bv_mnit_2")
myMQTTClient.connect()

def default_callback(client, userdata, message):
    print("received message", message)

class AwsIoTSubscriber(AwsIoTClient):
    def __init__(self, clientId, root_cert_path, private_key_path, device_cert_path, endpoint):
        AwsIoTClient.__init__(self, clientId, root_cert_path, private_key_path, device_cert_path, endpoint)

    def subscribe_client(self, topic, qos=1, calback=default_callback):
        self.aws_client.subscribe(topic, qos, calback)
