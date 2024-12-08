from loguru import logger
from quixstreams import Application
from quixstreams.sinks.core.csv import CSVSink


def main(
    kafka_broker_address: str,
    kafka_input_topic: str,
    kafka_consumer_group: str,
    feature_group_name: str,
    feature_group_version: int,
):
    """
    2 things:
    - Read from a Kafka topic
    - Write to a feature store
    """

    logger.info('Hello from to-feature-store!')

    # TODO quixstreams

    # Create a new application
    app = Application(
        broker_address=kafka_broker_address,
        consumer_group=kafka_consumer_group,
    )

    # Define the input and output topics of our streaming application
    input_topic = app.topic(
        name=kafka_input_topic,
        value_deserializer='json',
    )

    # Initialize a CSV sink with a file path
    csv_sink = CSVSink(path='tech_indica.csv')

    sdf = app.dataframe(input_topic)
    # Do some processing here ...
    # Sink data to a CSV file
    sdf.sink(csv_sink)

    app.run()

    # TODO hopsworks
    # push data to feature store


if __name__ == '__main__':
    from config import config

    main(
        kafka_broker_address=config.kafka_broker_address,
        kafka_input_topic=config.kafka_input_topic,
        kafka_consumer_group=config.kafka_consumer_group,
        feature_group_name=config.feature_group_name,
        feature_group_version=config.feature_group_version,
    )
