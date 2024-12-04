from datetime import timedelta
from typing import Any, List, Optional, Tuple
from loguru import logger
from quixstreams.models import TimestampType
from quixstreams import Application
from config import config


def init_candle(trade: dict) -> dict:
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

 # 1. Define the parameters of the function
def main(
    KAFKA_BROKER_ADDRESS: str,
    KAFKA_INPUT_TOPIC: str,
    KAFKA_OUTPUT_TOPIC: str,
    KAFKA_CONSUMER_GROUP: str,
    CANDLE_SECONDS: int,
       
):
    """
    3 steps:
    1. Ingests trades from Kafka
    2. Generates candles using tumbling windows and
    3. Outputs candles to Kafka

    Args: 

    KAFKA_BROKER_ADDRESS: Redpanda broker address
    KAFKA_INPUT_TOPIC: Input topic
    KAFKA_OUTPUT_TOPIC: Output topic
    KAFKA_CONSUMER_GROUP: Consumer group
    CANDLE_SECONDS: Candle time in seconds

    Returns:
        None
    """

    logger.info('Starting the candles service!')






if __name__ == "__main__":

    main(
        KAFKA_BROKER_ADDRESS=config.KAFKA_BROKER_ADDRESS,
        KAFKA_INPUT_TOPIC=config.KAFKA_INPUT_TOPIC,
        KAFKA_OUTPUT_TOPIC=config.KAFKA_OUTPUT_TOPIC,
        KAFKA_CONSUMER_GROUP=config.KAFKA_CONSUMER_GROUP,
        CANDLE_SECONDS=config.CANDLE_SECONDS,
    )




        # 2. Define the function
        # 3. Call the function
        # 4. Return the result
        # 5. Print the result
        # 6. Save the result
        # 7. Return the result