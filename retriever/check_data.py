from retriever.dal import Dal
import time
from kafka import KafkaProducer
from bson import json_util
import json


class GetData:


    dal = Dal()
    collection = dal.open_connection()

    def get_collection(self):
        lenght = self.collection.count_documents({})
        current_jmp = 0
        try:
            while current_jmp < lenght:
                tweets = list(self.collection.find({}).skip(current_jmp).limit(100).sort('CreateDate', 1))
                tweets = json.dumps(tweets, default=json_util.default)
                filtering = self.filter_data(json.loads(tweets))
                producer = self.get_producer()
                self.publish_message(producer, "raw_tweets_antisemitic", filtering["tweets_antisemitic"])
                self.publish_message(producer, "raw_tweets_not_antisemitic", filtering["tweets_not_antisemitic"])

                print("Message sent to Kafka") 
                current_jmp += 100
                time.sleep(60)
                print("sleep 60 second")  
        except Exception as e:
            print(e)
    

    def filter_data(self, list_tweets):
        tweets_antisemitic = list()
        tweets_not_antisemitic = list()

        for tweet in list_tweets:
            if tweet["Antisemitic"] == 1:
                tweets_antisemitic.append(tweet)
            else:
                tweets_not_antisemitic.append(tweet)

        return {"tweets_antisemitic": tweets_antisemitic,
                "tweets_not_antisemitic": tweets_not_antisemitic}


    def get_producer(self):
        return KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def publish_message(self, producer, topic, message):
        producer.send(topic, message)
        producer.flush()


a = GetData()

a.get_collection()