from config import aws_credentials, config
from loguru import logger
from quixstreams import Application
from quixstreams.sinks.community.file import FileSink
from quixstreams.sinks.community.file.destinations import S3Destination
from quixstreams.sinks.community.file.formats import JSONFormat


def main(
    kafka_broker_address: str,
    kafka_input_topic: str,
    kafka_consumer_group: str,
    feature_group_name: str,
    feature_group_version: int,
    aws_access_key_id: str,
    aws_secret_access_key: str,
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

    # Configure the sink to write JSON files to S3
    file_sink = FileSink(
        # # Optional: defaults to current working directory
        # directory="data",
        # Optional: defaults to "json"
        # Available formats: "json", "parquet" or an instance of Format
        format=JSONFormat(compress=True),
        destination=S3Destination(
            bucket='realtimeml',
            # Optional: AWS credentials
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name='us-east-1',
        ),
    )

    sdf = app.dataframe(topic=input_topic)
    sdf.sink(file_sink)

    app.run()


if __name__ == '__main__':
    main(
        kafka_broker_address=config.kafka_broker_address,
        kafka_input_topic=config.kafka_input_topic,
        kafka_consumer_group=config.kafka_consumer_group,
        feature_group_name=config.feature_group_name,
        feature_group_version=config.feature_group_version,
        aws_access_key_id=aws_credentials.aws_access_key_id,
        aws_secret_access_key=aws_credentials.aws_secret_access_key,
    )
