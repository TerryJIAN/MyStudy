# -*- coding: utf-8 -*-
from time import sleep
from json import dumps
from kafka import KafkaProducer
import time

data =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
producer = KafkaProducer(bootstrap_servers=['192.168.105.49:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in data:
    data = {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) : e}
    producer.send('testTopic', value=data)
    sleep(0.5)
