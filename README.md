pyeurofx
=============
.. image:: https://travis-ci.org/supercoderz/pyeurofx.svg?branch=master
	:target: https://travis-ci.org/supercoderz/pyeurofx


This is a simple module that fetches the daily and historical FX rates from ECB and parses the data.
The data is downloaded as XML files and returned as a list of (symbol, date, rate) tuples.
There is also the option to get the data as a pandas data frame.

Install this module using 'pip install pyeurofx'

This works with python 2.x and 3.x

This depends on 3 modules - requests, lxml and pandas.

pandas is required to be be able to get the data as a data frame.

The daily data is the last close price updated at 3 PM CET. The historical data is the daily close
price for every day since 1 Jan 1999.

The data fetched will be the rates for EUR vs all major currencies.

To use the module, do something like this - 

```python
import eurofx

daily = get_daily_data()
historical = get_historical_data()

daily_df = get_daily_data_df()
historical_df = get_historical_data_df()

```

To see a ipython notebook example, visit - http://nbviewer.ipython.org/github/supercoderz/pyeurofx/blob/master/eurofx%20example.ipynb