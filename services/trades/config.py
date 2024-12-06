from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    Configuration class for managing application settings using environment variables.
    """

    # Load settings from an `.env` file with UTF-8 encoding.
    model_config = SettingsConfigDict(
        env_file='settings.env', env_file_encoding='utf-8'
    )

    # Required configuration fields:
    kafka_broker_address: str  # Address of the Kafka broker (e.g., "localhost:9092").
    kafka_topic: str  # Kafka topic to which messages will be sent (e.g., "trades").
    pairs: List[str]  # List of trading pairs to process (e.g., ["BTC/USD", "ETH/USD"]).


# Create a global instance of the `Config` class to be used throughout the application.
config = Config()
