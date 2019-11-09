from src.libs.aws_client import AwsIoTClient

class AwsIoTPublisher(AwsIoTClient):

    def __init__(self, clientId, root_cert_path, private_key_path, device_cert_path, endpoint):
        AwsIoTClient.__init__(self, clientId, root_cert_path, private_key_path, device_cert_path, endpoint)

    def publish_message(self, topic, payload, qos=1):
        self.aws_client.publish(topic, payload, qos)



