import sys
import os

from src.libs.config_parser import IotConfigParser

config_path = os.path.join(os.getcwd(), "config.ini")
config = IotConfigParser(config_path)

# Session 1
# ------------------------------------------------------------------------------------------------------------------
session_1_config = config.get_section("SESSION_1")


'''
Uncomment the code below to publish your first message
'''
from src.session_1.basic_pub import PahoPublisher
publisher = PahoPublisher(session_1_config["BROKER_URL"])
publisher.publish_message("test/topic", "my_test")


'''
Uncomment the code below to run a simple publisher and subscriber on thread
'''
# import threading
# import time
#
# from src.session_1.basic_pub import PahoPublisher
# from src.session_1.basic_sub import PahoSubscriber
#
# publisher = PahoPublisher(session_1_config["BROKER_URL"])
# subscriber = PahoSubscriber(session_1_config["BROKER_URL"])
#
# def publish_message(topic, message, timeout=10):
#     start_time = time.time()
#     while True and time.time() <= start_time + timeout:
#         publisher.publish_message(topic, message)
#         time.sleep(1)
#
#
# def subscribe_topic(topic, timeout=5):
#     subscriber.subscribe_topic(topic, timeout)
#
# pub_thread = threading.Thread(target=publish_message, args=("bitvivid/test/topic", "test_message",5))
# sub_thread = threading.Thread(target=subscribe_topic, args=("bitvivid/test/topic", 5))
#
# pub_thread.start()
# sub_thread.start()
#
# pub_thread.join()
# sub_thread.join()
#
# print("Exiting --->")

#--------------------------------------------------------------------------------------------------------------