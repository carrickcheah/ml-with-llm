# Mock the Kraken API
from datetime import datetime
from typing import List
from time import sleep

from .trade import Trade


class KrakenMockAPI:
    """
    A mock implementation of the Kraken API for testing purposes.
    """

    def __init__(self, pair: str):
        """
        Initializes the mock Kraken API.
        - `pair`: The trading pair (e.g., "BTC/USD") to simulate trades for.
        """
        self.pair = pair

    def get_trades(self) -> List[Trade]:
        """
        Simulates fetching a list of trades for the specified trading pair.
        - Returns two hardcoded `Trade` objects representing mock trades.
        - Includes a delay of 1 second to mimic real-world API latency.
        """
        mock_trades = [
            Trade(
                pair=self.pair,
                price=0.5117,
                volume=40.0,
                timestamp=datetime(2023, 9, 25, 7, 49, 37, 708706),
                timestamp_ms=172719357708706,
            ),
            Trade(
                pair=self.pair,
                price=0.5317,
                volume=40.0,
                timestamp=datetime(2023, 9, 25, 7, 49, 37, 708706),
                timestamp_ms=172719357708706,
            ),
        ]

        sleep(1)

        return mock_trades
