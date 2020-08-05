# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'testTopic',
     bootstrap_servers=['192.168.105.49:9092'],
     auto_offset_reset='earliest',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('{}'.format(message))