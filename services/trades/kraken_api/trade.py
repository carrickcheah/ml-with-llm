from datetime import datetime
from pydantic import BaseModel
# from typing import Optional


class Trade(BaseModel):
    """
    A trade from the Kraken API.
    """

    pair: str
    price: float
    volume: float
    timestamp: datetime
    timestamp_ms: int

    @classmethod
    def from_kraken_api_response(
        cls,
        pair: str,
        price: float,
        volume: float,
        timestamp: datetime,
    ) -> "Trade":
        """
        This class method allows creating a `Trade` object directly from raw Kraken API response data.
        - Takes the raw fields (`pair`, `price`, etc.) from the response.
        - Calls the class constructor to create an instance of the `Trade` class.
        - Converts the `timestamp` into milliseconds using `_datestr2milliseconds` to store it as `timestamp_ms`.
        """
        return cls(
            pair=pair,
            price=price,
            volume=volume,
            timestamp=timestamp,
            timestamp_ms=cls._datestr2milliseconds(timestamp),
        )

    @staticmethod
    def _datestr2milliseconds(datestr: str) -> int:
        """
        Converts a timestamp string in ISO format into a Unix timestamp in milliseconds.
        - Parses the ISO string using `datetime.strptime`.
        - Converts the resulting `datetime` object to a Unix timestamp and multiplies it by 1000 for milliseconds.
        """
        return int(
            datetime.strptime(datestr, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp() * 1000
        )

    def to_str(self) -> str:
        """
        Converts the `Trade` object into a JSON string using pydantic's built-in serialization.
        - Useful for sending the object as a message or storing it in text format.
        """
        return self.model_dump_json()
