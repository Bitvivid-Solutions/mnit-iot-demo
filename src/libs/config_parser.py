import configparser

config = configparser.ConfigParser()
config.read('../../config.ini')

broker = config["BROKER"]["BROKER_URL"] or "mqtt.eclipse.org"
topic = config["TOPICS"]["INITIAL_TOPIC"] or "test"