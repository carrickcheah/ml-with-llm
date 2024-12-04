# Build second microservices

This microservice reads data from the 'trades' Kafka topic, and stores it in the 'candles' Kafka topic.  
Utilizing the Redpanda streaming platform necessitates specifying the Kafka broker address and a consumer group.  
The module processes data over 60-second windows.  

       - KAFKA_BROKER_ADDRESS=
       - KAFKA_INPUT_TOPIC=
       - KAFKA_OUTPUT_TOPIC=
       - KAFKA_CONSUMER_GROUP=
       - CANDLE_SECONDS=

## Init new project

bash$   uv init candles

## Create config, settings.env, and Makefile

Setup the credentials  

## Start logic in run.py



