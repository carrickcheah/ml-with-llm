# Session 3

Today tasks:  

- dockerize candles

## dockerize candles

copy the trades dockerfile since it is same. and update Makefile  


## Feature engineering - add technical-indicators

- bash$   uv init --no-workspace technical-indicators
        uv add quixstreams loguru pydantic-settings

- Install ta-lib  
        Bash$ uv add TA-Lib
        i get this version ta-lib>=0.5.1 , but not limit to.

if canot, thn add
Linux
Download ta-lib-0.4.0-src.tar.gz and:

$ tar -xzf ta-lib-0.4.0-src.tar.gz
$ cd ta-lib/
$ ./configure --prefix=/usr
$ make
$ sudo make install



- Just use quixstream connect input n output first.

## Technical indicators service - Part 3

solve problem: candle.py, create 2 functions


refer session_03b.md



## To feature store
Read message from topic and push data to feature store






# Flowchart run.py
"""
+----------------------------------------------------------------------------------------+
|                                      Start                                             |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Log the startup message                                                               |
| logger.info('Hello from technical-indicators!')                                         |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Initialize Kafka Application                                                           |
| app = Application(                                                                       |
|     broker_address=kafka_broker_address,                                                  |
|     consumer_group=kafka_consumer_group,                                                  |
| )                                                                                      |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Define the input Kafka topic                                                           |
| input_topic = app.topic(                                                                  |
|     name=kafka_input_topic,                                                               |
|     value_deserializer='json',                                                            |
| )                                                                                      |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Define the output Kafka topic                                                          |
| output_topic = app.topic(                                                                 |
|     name=kafka_output_topic,                                                              |
|     value_serializer='json',                                                             |
| )                                                                                      |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Create a Streaming DataFrame from the input topic                                      |
| sdf = app.dataframe(topic=input_topic)                                                    |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Apply the `update_candles` function to update the list of candles in the state         |
| sdf = sdf.apply(update_candles, stateful=True)                                           |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Apply the `compute_indicators` function to compute technical indicators                |
| sdf = sdf.apply(compute_indicators, stateful=True)                                        |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Log the final message containing the candle and computed indicators                    |
| sdf = sdf.update(lambda value: logger.debug(f'Final message: {value}'))                   |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Send the processed data with technical indicators to the output Kafka topic            |
| sdf = sdf.to_topic(output_topic)                                                           |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
| # Run the Kafka Streaming Application                                                    |
| app.run()                                                                                |
+----------------------------------------------------------------------------------------+
                                          |
                                          v
+----------------------------------------------------------------------------------------+
|                                      End                                               |
+----------------------------------------------------------------------------------------+

"""





# Flowchart technical_indicators.py
"""
+----------------------------------------------------------+
|                      Start                               |
+----------------------------------------------------------+
                          |
                          v
+----------------------------------------------------------+
| # Retrieve the list of candles from the state           |
| candles = state.get('candles', [])                      |
+----------------------------------------------------------+
                          |
                          v
+----------------------------------------------------------+
| # Extract open, high, low, close, and volume as arrays  |
| high = [candle['high'] for candle in candles]           |
| low = [candle['low'] for candle in candles]             |
| close = [candle['close'] for candle in candles]         |
| volume = [candle['volume'] for candle in candles]       |
+----------------------------------------------------------+
                          |
                          v
+----------------------------------------------------------+
| # Initialize an empty dictionary to store indicators     |
| indicators = {}                                          |
+----------------------------------------------------------+
                          |
                          v
+---------------------------- Compute Indicators -----------------------------+
| RSI (Relative Strength Index):                                             |
| indicators['rsi_9'], ['rsi_14'], ['rsi_21']                                |
| MACD (Moving Average Convergence Divergence):                              |
| indicators['macd'], ['macd_signal'], ['macd_hist']                         |
| Bollinger Bands (BBANDS):                                                  |
| indicators['bbands_upper'], ['bbands_middle'], ['bbands_lower']            |
| Stochastic RSI (STOCHRSI):                                                 |
| indicators['stochrsi_fastk'], ['stochrsi_fastd']                           |
| ADX (Average Directional Index):                                           |
| indicators['adx']                                                          |
| Volume EMA:                                                                |
| indicators['volume_ema']                                                   |
| Ichimoku Cloud Components:                                                 |
| indicators['ichimoku_conv'], ['ichimoku_base'],                            |
| ['ichimoku_span_a'], ['ichimoku_span_b']                                   |
| Money Flow Index (MFI):                                                    |
| indicators['mfi']                                                          |
| Average True Range (ATR):                                                  |
| indicators['atr']                                                          |
| Price Rate of Change (ROC):                                                |
| indicators['price_roc']                                                    |
| Simple Moving Averages (SMA):                                              |
| indicators['sma_7'], ['sma_14'], ['sma_21']                                |
+----------------------------------------------------------------------------+
                          |
                          v
+----------------------------------------------------------+
|# Merge the latest candle with the computed indicators    |
| final_message = {**candle, **indicators}                 |
+----------------------------------------------------------+
                          |
                          v
+----------------------------------------------------------+
|# Return the final message containing the candle and      |
| all computed indicators                                  |
+----------------------------------------------------------+
                          |
                          v
+----------------------------------------------------------+
|                          End                             |
+----------------------------------------------------------+

"""







candle.py
# 1. Flowchart : update_candles
"""
+--------------------------------------------------------------+
|                         Start                                |
+--------------------------------------------------------------+
                              |
                              v
+--------------------------------------------------------------+
|# Retrieve existing candles from state                        |
| candles = state.get('candles', default=[])                   |
+--------------------------------------------------------------+
                              |
                              v
+--------------------------+-------------------------------+
| Is the record book empty?                                |
| (Are there no existing candles?)                         |
+--------------------------+-------------------------------+
             | Yes                                     | No
             v                                         v
+--------------------------+          +--------------------------+
| Append the new candle    |          | Check if new candle      |
| candles.append(candle)   |          | belongs to the same      |
|                          |          | time window as last      |
+--------------------------+          | candle                   |
             |                        | same_window(candle,      |
             |                        | candles[-1])?            |
             v                        +--------------------------+
+--------------------------+                        |
| Proceed to manage        |                        |
| capacity and update      |                        |
| state                    |                        |
+--------------------------+                        |
             |                                      |
             v                                      v
+--------------------------+          +--------------------------+
| Replace the last candle  |          | Append the new candle    |
| with the new candle     |           | to the list              |
| candles[-1] = candle    |           | candles.append(candle)   |
+--------------------------+          +--------------------------+
             |                                      |
             |                                      |
             +----------------------+---------------+
                                    |
                                    v
+--------------------------------------------------------------+
| Is the number of candles > MAX_CANDLES_IN_STATE?             |
+--------------------------+-----------------------------------+
             | Yes                                     | No
             v                                         v
+--------------------------+          +--------------------------+
| Remove the oldest candle |          | Proceed to log and       |
| candles.pop(0)           |          | update state             |
+--------------------------+          +--------------------------+
             |                                      |
             |                                      |
             +----------------------+---------------+
                                    |
                                    v
+--------------------------------------------------------------+
| Log the current number of candles                           |
| logger.debug(f'Number of candles in state for {candle["pair"]}: {len(candles)}') |
+--------------------------------------------------------------+
                              |
                              v
+--------------------------------------------------------------+
| Update the state with the new list of candles               |
| state.set('candles', candles)                               |
+--------------------------------------------------------------+
                              |
                              v
+--------------------------------------------------------------+
| Return the updated candle                                    |
| return candle                                                |
+--------------------------------------------------------------+
                              |
                              v
+--------------------------------------------------------------+
|                          End                                 |
+--------------------------------------------------------------+

"""

# 2. Flowchart : same_window

"""

+----------------------------------------+
|             Start                      |
+----------------------------------------+
                |
                v
+----------------------------------------+
| Compare window_start_ms of both candles|
| candle_1['window_start_ms'] ==         |
| candle_2['window_start_ms']            |
+----------------------------------------+
                |
                v
+----------------------------------------+
| Compare window_end_ms of both candles  |
| candle_1['window_end_ms'] ==           |
| candle_2['window_end_ms']              |
+----------------------------------------+
                |
                v
+----------------------------------------+
| Compare pair of both candles           |
| candle_1['pair'] == candle_2['pair']   |
+----------------------------------------+
                |
                v
+----------------------------------------+
| All comparisons True?                  |
| (window_start_ms, window_end_ms, pair) |
+----------------------+-----------------+
           | Yes                        | No
           v                            v
+--------------------------+   +--------------------------+
| Return True              |   | Return False             |
+--------------------------+   +--------------------------+
                |
                v
+----------------------------------------+
|               End                      |
+----------------------------------------+

"""
