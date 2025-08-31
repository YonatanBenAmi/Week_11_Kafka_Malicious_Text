import cleaner
from kafka import KafkaProducer
import json


class Manager:
    def __init__(self):
        # מגדירים producer פעם אחת
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def clean(self,data,source_topic):
        clean=cleaner.Cleaner()
        for message in data:
            text = message["text"]
            text = clean.Removing_stop_words(text)
            text = clean.Remove_special_characters(text)
            text = clean.Removing_unnecessary_whitespace_characters(text)
            text = clean.Converting_text_to_lowercase(text)
            text = clean.Removing_stop_words(text)
            text = clean.Lemtization(text)
            message["clean text"] = text
            message["original_text"]=message.pop("text")
            print(message)


        # שליחה ל־Kafka לטופיק המתאים
            if source_topic == "raw_tweets_antisemitic":
                self.send_to_kafka("preprocessed_tweets_antisemitic", message)
            elif source_topic == "raw_tweets_not_antisemitic":
                self.send_to_kafka("preprocessed_tweets_not_antisemitic", message)

    def send_to_kafka(self, topic, message):
        self.producer.send(topic, message)
        self.producer.flush()
        print(f"sent to {topic}: {message}")







