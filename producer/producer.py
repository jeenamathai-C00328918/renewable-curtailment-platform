from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

print("Starting producer...")

try:
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    print("Connected to Kafka!")

except Exception as e:
    print("Kafka connection failed:")
    print(e)
    exit()

while True:

    try:
        print("Generating data...")

        data = {
            "timestamp": datetime.now().isoformat(),
            "wind_generation": random.randint(1500, 3500),
            "electricity_demand": random.randint(3000, 6000)
        }

        print("Data:", data)

        future = producer.send(
           "renewable-energy",
              value=data
            )

        record_metadata = future.get(timeout=10)

        print(record_metadata)

        producer.flush()
        print("--------------------------------")

        time.sleep(5)

    except Exception as e:
        print("Error occurred:")
        print(e)
        break