import numpy as np
from quixstreams import State
from talib import stream


def compute_indicators(
    candle: dict,
    state: State,
) -> dict:
    """
    Computes the technical indicators from the candles in the state
    """
    candles = state.get('candles', [])

    # Extract open, high, low, close, volume from the candles
    # open = np.array([c['open'] for c in candles])
    # high = np.array([c['high'] for c in candles])
    # low = np.array([c['low'] for c in candles])
    close = np.array([c['close'] for c in candles])
    volume = np.array([c['volume'] for c in candles])

    indicators = {}

    # -------------------------
    # Math Transform Functions
    # -------------------------
    # Note: Some mathematical transformations like ACOS and ASIN require inputs in the range [-1, 1].
    # Ensure your data meets these requirements or handle exceptions appropriately.

    # Applying mathematical transformations to the 'close' price
    # Clip the close prices to the valid range for ACOS and ASIN to avoid errors
    close_clipped = np.clip(close, -1, 1)

    indicators['ACOS'] = stream.ACOS(close_clipped)  # ACOS - Vector Trigonometric ACos
    indicators['ASIN'] = stream.ASIN(close_clipped)  # ASIN - Vector Trigonometric ASin
    indicators['ATAN'] = stream.ATAN(close)  # ATAN - Vector Trigonometric ATan
    indicators['CEIL'] = stream.CEIL(close)  # CEIL - Vector Ceil
    indicators['COS'] = stream.COS(close)  # COS - Vector Trigonometric Cos
    indicators['COSH'] = stream.COSH(close)  # COSH - Vector Trigonometric Cosh
    indicators['EXP'] = stream.EXP(close)  # EXP - Vector Arithmetic Exp
    indicators['FLOOR'] = stream.FLOOR(close)  # FLOOR - Vector Floor
    indicators['LN'] = stream.LN(close)  # LN - Vector Log Natural
    indicators['LOG10'] = stream.LOG10(close)  # LOG10 - Vector Log10
    indicators['SIN'] = stream.SIN(close)  # SIN - Vector Trigonometric Sin
    indicators['SINH'] = stream.SINH(close)  # SINH - Vector Trigonometric Sinh
    indicators['SQRT'] = stream.SQRT(
        close_clipped + 1
    )  # SQRT - Vector Square Root (added 1 to avoid sqrt(0))
    indicators['TAN'] = stream.TAN(close)  # TAN - Vector Trigonometric Tan
    indicators['TANH'] = stream.TANH(close)  # TANH - Vector Trigonometric Tanh

    # ----------------------------
    # Math Operator Functions
    # ----------------------------
    # Ensure that 'indicators0' and 'indicators1' are defined as numpy arrays
    # For demonstration, we'll use 'close' and 'volume' as indicators0 and indicators1

    indicators0 = close
    indicators1 = volume

    indicators['ADD'] = stream.ADD(
        indicators0, indicators1
    )  # ADD - Vector Arithmetic Add
    indicators['DIV'] = stream.DIV(
        indicators0, indicators1
    )  # DIV - Vector Arithmetic Div
    indicators['MAX'] = stream.MAX(
        close, timeperiod=30
    )  # MAX - Highest value over a specified period
    indicators['MAXINDEX'] = stream.MAXINDEX(
        close, timeperiod=30
    )  # MAXINDEX - Index of highest value over a specified period
    indicators['MIN'] = stream.MIN(
        close, timeperiod=30
    )  # MIN - Lowest value over a specified period
    indicators['MININDEX'] = stream.MININDEX(
        close, timeperiod=30
    )  # MININDEX - Index of lowest value over a specified period
    indicators['MINMAX'] = stream.MINMAX(
        close, timeperiod=30
    )  # MINMAX - Lowest and highest values over a specified period
    indicators['MINMAXINDEX'] = stream.MINMAXINDEX(
        close, timeperiod=30
    )  # MINMAXINDEX - Indexes of lowest and highest values over a specified period
    indicators['MULT'] = stream.MULT(
        indicators0, indicators1
    )  # MULT - Vector Arithmetic Mult
    indicators['SUB'] = stream.SUB(
        indicators0, indicators1
    )  # SUB - Vector Arithmetic Subtraction
    indicators['SUM'] = stream.SUM(
        close, timeperiod=30
    )  # SUM - Summation over a specified period

    # ----------------------------
    # Regression and Statistical Functions
    # ----------------------------
    indicators['BETA'] = stream.BETA(
        close, volume, timeperiod=5
    )  # BETA - Measures the covariance of two indicators normalized by variance
    indicators['CORREL'] = stream.CORREL(
        close, volume, timeperiod=30
    )  # CORREL - Pearson's Correlation Coefficient (r) over a specified period
    indicators['LINEARREG'] = stream.LINEARREG(
        close, timeperiod=14
    )  # LINEARREG - Linear Regression value over a specified period
    indicators['LINEARREG_ANGLE'] = stream.LINEARREG_ANGLE(
        close, timeperiod=14
    )  # LINEARREG_ANGLE - Angle of the linear regression line over a specified period
    indicators['LINEARREG_INTERCEPT'] = stream.LINEARREG_INTERCEPT(
        close, timeperiod=14
    )  # LINEARREG_INTERCEPT - Intercept of the linear regression line over a specified period
    indicators['LINEARREG_SLOPE'] = stream.LINEARREG_SLOPE(
        close, timeperiod=14
    )  # LINEARREG_SLOPE - Slope of the linear regression line over a specified period
    indicators['STDDEV'] = stream.STDDEV(
        close, timeperiod=5, nbdev=1
    )  # STDDEV - Standard deviation of values over a specified period
    indicators['TSF'] = stream.TSF(
        close, timeperiod=14
    )  # TSF - Time Series Forecast value based on linear regression
    indicators['VAR'] = stream.VAR(
        close, timeperiod=5, nbdev=1
    )  # VAR - Variance of values over a specified period

    # ----------------------------
    # Handle Potential NaNs or Infinities
    # ----------------------------
    for key in indicators:
        if isinstance(indicators[key], np.ndarray):
            indicators[key] = np.nan_to_num(
                indicators[key], nan=0.0, posinf=0.0, neginf=0.0
            )

    # ----------------------------
    # Emit Final Message
    # ----------------------------
    final_message = {
        **candle,
        **indicators,
    }
    return final_message
