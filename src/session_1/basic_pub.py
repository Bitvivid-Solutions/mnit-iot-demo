from src.libs.paho_client import paho_client
from src.libs.config_parser import topic


def pub_callback(client, userdata, mid):
    print("message was sent successfully")


paho_client.on_publish = pub_callback
# This message will be sent over the topic
payload = "test"

pub = paho_client.publish(topic, payload)
