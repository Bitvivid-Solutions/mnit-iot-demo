from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

class AwsIoTClient:
    def __init__(self, clientId, root_cert_path, private_key_path, device_cert_path, endpoint="a3kzkg384kgksx-ats.iot.ap-south-1.amazonaws.com"):
        self.__root_cert_path__ = root_cert_path
        self.__private_key_path__= private_key_path
        self.__device_cert__ = device_cert_path
        self.client_id = clientId
        self.endpoint = endpoint
        self.aws_client = self.__get_aws_client__()
        self.aws_client.connect()

    def __get_aws_client__(self, port=443, drain_freq=2, connect_timeout=10, operation_timeout=5):
        myMQTTClient = AWSIoTMQTTClient(self.client_id)
        myMQTTClient.configureEndpoint(self.endpoint, port)
        myMQTTClient.configureCredentials(self.__root_cert_path__, self.__private_key_path__, self.__device_cert__)
        myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        myMQTTClient.configureDrainingFrequency(drain_freq)  # Draining: 2 Hz
        myMQTTClient.configureConnectDisconnectTimeout(connect_timeout)  # 10 sec
        myMQTTClient.configureMQTTOperationTimeout(operation_timeout)  # 5 sec
        return myMQTTClient

