from kafka import KafkaConsumer
import json

def consume_message(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    messages = []
    for msg in consumer:
        messages.append(json.loads(msg.value.decode('utf-8')))
        break  # Only consume one for simplicity
    return messages
