class EnrichHandler:
    def __init__(self, sentiment_processor, weapons_detector=None, producer=None, output_topic=None, timestamp_extractor=None):
        self.sp = sentiment_processor
        self.wp = weapons_detector
        self.producer = producer
        self.output_topic = output_topic
        self.ts = timestamp_extractor



    def handle(self, message):
        if isinstance(message, list):
            for item in message:
                self._process_one(item)
            return message
        return self._process_one(message)


    def _process_one(self, msg: dict):
        if not isinstance(msg, dict):
            print(f"[EnrichHandler] Skipping non-dict message of type {type(msg)}")
            return msg

        clean_text = msg.get("clean_text", "")
        original_text = msg.get("original_text", "")

        msg["sentiment"] = self.sp.get_sentiment(clean_text)

        if self.wp and hasattr(self.wp, "find_weapons"):
            msg["weapons_detected"] = self.wp.find_weapons(clean_text) or []
        elif self.wp:
            first = self.wp.find_weapon(clean_text)
            msg["weapons_detected"] = ([first] if first else [])
        else:
            msg["weapons_detected"] = msg.get("weapons_detected", [])

        # msg["relevant_timestamp"] = self.ts.extract(original_text) if self.ts else msg.get("relevant_timestamp", "")
        msg["relevant_timestamp"] = self.ts.extract(original_text) if self.ts else msg.get("relevant_timestamp", "")
        print(
            f"[enriched] id={msg.get('id')} sentiment={msg['sentiment']} weapons={msg['weapons_detected']} date={msg.get('relevant_timestamp', '')}")

        assert msg.get("sentiment") in {"positive", "neutral", "negative"}
        assert isinstance(msg.get("weapons_detected"), list)
        print(f"[enriched] id={msg.get('id')} sentiment={msg['sentiment']} weapons={msg['weapons_detected']} ts={msg.get('relevant_timestamp','')}")

        if self.producer and self.output_topic:
            key = str(msg.get("id")) if msg.get("id") is not None else None
            self.producer.publish(self.output_topic, msg, key=key)


        print(f"[enriched] sentiment={msg.get('sentiment')} weapons={msg.get('weapons_detected')}")
        return msg


        return msg
