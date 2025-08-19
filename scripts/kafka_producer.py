from kafka import KafkaProducer
import json

def produce_message(topic, message):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    producer.send(topic, json.dumps(message).encode('utf-8'))
    producer.flush()
    return {'status': 'message_sent', 'topic': topic}
