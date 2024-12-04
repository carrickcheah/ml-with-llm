from typing import List
import json
from loguru import logger
from websocket import create_connection
from .trade import Trade

class KrakenWebsocketAPI:

    URL = "wss://ws.kraken.com/v2"

    def __init__(self, pairs: List[str]):
        self.pairs = pairs

        # create a websocket client
        self._ws_client = create_connection(self.URL)

        # subscribe to the websocket
        self._subscribe()

    #   This is the __init__ method, which sets up the WebSocket connection when you create an instance of KrakenWebsocketAPI.
    # - `self.pairs`: Stores the trading pairs you want to track.
    # - `self._ws_client`: Connects to the WebSocket server using the provided URL.
    # - `self._subscribe()`: Subscribes to trade updates for the specified trading pairs.

    def get_trades(self) -> List[Trade]:
        """
        Fetches the trades fromm the Kraken Websocket APIs and returns them as a list of Trade objects.

        Returns:
            List[Trade]: A list of Trade objects.
        """
        # receive the data from the websocket
        data = self._ws_client.recv()

        if 'heartbeat' in data:
            logger.info("Heartbeat received")
            return []
        
        # transform raw string into a JSON object
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
            return []

        try:
            trades_data = data['data']
        except KeyError as e:
            logger.error(f"No `data` field with trades in the message {e}")
            return []

        trades = [
            Trade.from_kraken_api_response(
                pair=trade['symbol'],
                price=trade['price'],
                volume=trade['qty'],
                timestamp=trade['timestamp'],
            ) for trade in trades_data
        ]
        # breakpoint()
        return trades

    # This is the `get_trades` method, which fetches and processes trade data from the Kraken WebSocket server.
    # - Receives data from the WebSocket server using `_ws_client.recv()`.
    # - Checks for "heartbeat" messages (signals the server is active but no data is sent yet).
    # - Processes trade data from the server and converts it into a list of `Trade` objects using `from_kraken_api_response`.

    def _subscribe(self):
        """
        Subscribes to the websocket and waits for the initial snapshot.
        """
        # send a subscribe message to the websocket
        self._ws_client.send(json.dumps({
            "method": "subscribe",
            "params": {
                "channel": "trade",
                "symbol": self.pairs,
                "snapshot": True
            }
        }))

        for pair in self.pairs:
            _ = self._ws_client.recv()
            _ = self._ws_client.recv()


    # This is the `_subscribe` method, which subscribes to the WebSocket server for live trade updates.
    # - Sends a subscription message to the WebSocket server with details of the trading pairs you want to track.
    # - Listens for confirmation messages for each trading pair.

def datestr2milliseconds(iso_time: str) -> int:
    """
    Convert ISO format datetime string to Unix milliseconds timestamp.
    
    Args:
        iso_time (str): ISO format datetime string (e.g. '2023-09-25T07:49:37.708706Z')
    
    Returns:
        int: Unix timestamp in milliseconds
    """
    from datetime import datetime
    dt = datetime.strptime(iso_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    return int(dt.timestamp() * 1000)


# This is the `datestr2milliseconds` function, which converts an ISO format date string into a Unix timestamp in milliseconds.
# - Converts the string into a `datetime` object using `datetime.strptime`.
# - Converts the `datetime` object into a Unix timestamp (in seconds) and multiplies by 1000 to get milliseconds.
