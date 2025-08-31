import json
from kafka import KafkaProducer

class Producer:
    def __init__(self, bootstrap_servers="localhost:9092"):
        self.p = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            key_serializer=lambda k: (str(k).encode() if k is not None else None),
        )

    def publish(self, topic: str, value: dict, key: str | None = None):
        self.p.send(topic, value=value, key=key)
        # אפשר להוסיף self.p.flush() אם רוצים לחסום עד שליחה
