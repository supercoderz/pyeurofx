pyeurofx
=============

This is a simple module that fetches the daily and historical FX rates from ECB and parses the data.
The data is downloaded as XML files and returned as a list of (symbol, date, rate) tuples.

Install this module using 'pip install pyeurofx'

The daily data is the last close price updated at 3 PM CET. The historical data is the daily close
price for every day since 1 Jan 1999.

The data fetched will be the rates for EUR vs all major currencies

To use the module, do something like this - 

```python
import eurofx

daily = get_daily_data()
historical = get_historical_data()
```
