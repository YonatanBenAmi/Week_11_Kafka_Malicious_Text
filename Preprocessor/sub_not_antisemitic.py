import manager
from kafka import KafkaConsumer
import json

manager = manager.Manager()


def listen_kafka():
    consumer = KafkaConsumer(

        "raw_tweets_not_antisemitic",  # הטופיק של הלא אנטישמי
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',  # שיקרא מהתחלה אם לא קראנו עדיין
        enable_auto_commit=True,
        group_id="tweets-consumer-group",
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("listening")

    try:
        for message in consumer:
            print(f"[{message.topic}] {message.value}")
            manager.clean(message.value,message.topic)


    except KeyboardInterrupt:
        print("stopt thre lesenir ")


listen_kafka()