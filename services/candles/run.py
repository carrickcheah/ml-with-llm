from datetime import timedelta
from typing import Any, List, Optional, Tuple

from config import config
from loguru import logger
from quixstreams import Application
from quixstreams.models import TimestampType


# Define the candle window size in seconds
def init_candle(trade: dict) -> dict:  # trade is a dictionary.
    """
    Initialize a candle with the first trade
    """
    return {
        'open': trade['price'],
        'high': trade['price'],
        'low': trade['price'],
        'close': trade['price'],
        'volume': trade['volume'],
    }


def update_candle(candle: dict, trade: dict) -> dict:
    """
    Update the candle with the latest trade
    """
    candle['close'] = trade['price']
    candle['high'] = max(candle['high'], trade['price'])
    candle['low'] = min(candle['low'], trade['price'])
    candle['volume'] += trade['volume']
    return candle


# Define a custom timestamp extractor


def custom_ts_extractor(
    value: Any,
    headers: Optional[List[Tuple[str, bytes]]],
    timestamp: float,
    timestamp_type: TimestampType,
) -> int:
    """
    Specifying a custom timestamp extractor to use the timestamp from the message payload
    instead of Kafka timestamp.
    """
    # logger.debug(f'Custom timestamp extractor: {value}')
    return value['timestamp_ms']


def main(
    kafka_broker_address: str,
    kafka_input_topic: str,
    kafka_output_topic: str,
    kafka_consumer_group: str,
    candle_seconds: int,
    # emit_incomplete_candles: bool,
):
    """
    3 steps:
    1. Ingests trades from Kafka
    2. Generates candles using tumbling windows and
    3. Outputs candles to Kafka

    Args:
        kafka_broker_address (str): Kafka broker address
        kafka_input_topic (str): Kafka input topic
        kafka_output_topic (str): Kafka output topic
        kafka_consumer_group (str): Kafka consumer group
        candle_seconds (int): Candle seconds
        emit_incomplete_candles (bool): Emit incomplete candles or just the final one
    Returns:
        None
    """

    logger.info('Starting the candles service!')

    # Initialize the Quix Streams application.
    # This class handles all the low-level details to connect to Kafka.
    app = Application(
        broker_address=kafka_broker_address,
        consumer_group=kafka_consumer_group,
    )

    # Input and output value_serializer
    input_topic = app.topic(
        name=kafka_input_topic,
        value_deserializer='json',
        timestamp_extractor=custom_ts_extractor,
    )

    output_topic = app.topic(name=kafka_output_topic, value_serializer='json')

    # create a streaming dataframes from the input topic
    sdf = app.dataframe(input_topic)

    # Define a tumbling window
    sdf = sdf.tumbling_window(timedelta(seconds=candle_seconds))
    sdf = sdf.reduce(reducer=update_candle, initializer=init_candle)

    sdf = sdf.current()

    # push the candle to the output topic
    sdf = sdf.to_topic(topic=output_topic)

    # Start the application
    app.run()


if __name__ == '__main__':
    main(
        kafka_broker_address=config.kafka_broker_address,
        kafka_input_topic=config.kafka_input_topic,
        kafka_output_topic=config.kafka_output_topic,
        kafka_consumer_group=config.kafka_consumer_group,
        candle_seconds=config.candle_seconds,
        # emit_incomplete_candles=config.emit_incomplete_candles,
    )

    # 2. Define the function
    # 3. Call the function
    # 4. Return the result
    # 5. Print the result
    # 6. Save the result
    # 7. Return the result
