import paho.mqtt.client as mqtt
from src.libs.config_parser import broker

paho_client = mqtt.Client()
paho_client.connect(broker, 1883, 60)