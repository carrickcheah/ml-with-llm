from config import config
from loguru import logger
from quixstreams import Application


def main(
    kafka_broker_address: str,
    kafka_consumer_group: str,
    kafka_input_topic: str,
    kafka_output_topic: str,
    num_candles_in_state: int,
):
    print('Hello from technical-indicators!')

    app = Application(
        broker_address=kafka_broker_address,
        consumer_group=kafka_consumer_group,
    )

    # Define the input and output topics
    input_topic = app.topic(
        name=kafka_input_topic,
        value_deserializer='json',
    )
    output_topic = app.topic(
        name=kafka_output_topic,
        value_serializer='json',
    )

    sdf = app.dataframe(topic=input_topic)

    sdf = sdf.update(lambda value: logger.info(f'Candle: {value}'))
    sdf = sdf.to_topic(topic=output_topic)

    app.run()

    # def count_messages(value: dict, state: State):
    #     total = state.get('total', default=0)
    #     total += 1
    #     state.set('total', total)
    #     return {**value, 'total': total}

    # # Apply a custom function and inform StreamingDataFrame
    # # to provide a State instance to it using "stateful=True"
    # sdf = sdf.apply(count_messages, stateful=True)


if __name__ == '__main__':
    main(
        kafka_broker_address=config.kafka_broker_address,
        kafka_consumer_group=config.kafka_consumer_group,
        kafka_input_topic=config.kafka_input_topic,
        kafka_output_topic=config.kafka_output_topic,
        num_candles_in_state=config.num_candles_in_state,
    )
