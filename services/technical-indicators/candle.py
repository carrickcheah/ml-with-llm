from config import config
from loguru import logger
from quixstreams import State

MAX_CANDLES_IN_STATE = config.max_candles_in_state


def update_candles(
    candle: dict,
    state: State,
) -> dict:
    """
    Updates the list of candles we have in our state using the latest candle

    If the latest candle corresponds to a new window, and the total number
    of candles in the state is less than the number of candles we want to keep,
    we just append it to the list.

    If it corresponds to the last window, we replace the last candle in the list.

    Args:
        candle: The latest candle
        state: The state of our application
        max_candles_in_state: The maximum number of candles to keep in the state

    Returns:
        None
    """

    # Retrieve the list of existing candles from the application state.
    # If no candles exist in the state, initialize it as an empty list.
    candles = state.get('candles', default=[])

    # If the record book is empty, we just append the new candle
    if not candles:
        candles.append(candle)

    # If same_window is True, then we replace the last candle with the new candle
    # if same_window is False, then we append the new candle to the list
    elif same_window(candle, candles[-1]):
        candles[-1] = candle
    else:
        candles.append(candle)

    # If the number of candles is greater than the maximum number of candles we want to keep,
    # we remove the oldest candle
    if len(candles) > MAX_CANDLES_IN_STATE:
        candles.pop(0)

    logger.debug(f'Number of candles in state for {candle["pair"]}: {len(candles)}')

    # Update the state with the new list of candles
    state.set('candles', candles)

    # Return the updated candle
    return candle


def same_window(candle_1: dict, candle_2: dict) -> bool:
    """
    Check if candle_1 and candle_2 belong to the same time window and trading pair.

    Args:
        candle_1: The first candle
        candle_2: The second candle
    Returns:
        True if the candles are in the same window and pairs, False otherwise
    """
    return (
        candle_1['window_start_ms'] == candle_2['window_start_ms']
        and candle_1['window_end_ms'] == candle_2['window_end_ms']
        and candle_1['pair'] == candle_2['pair']
    )
