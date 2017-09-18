pyeurofx
=============

[![Travis](https://img.shields.io/travis/supercoderz/pyeurofx.svg?maxAge=2592000)](https://travis-ci.org/supercoderz/pyeurofx)
[![PyPI](https://img.shields.io/pypi/dw/pyeurofx.svg?maxAge=2592000)](https://pypi.python.org/pypi/pyeurofx)
[![PyPI](https://img.shields.io/pypi/v/pyeurofx.svg?maxAge=2592000)](https://pypi.python.org/pypi/pyeurofx)
[![PyPI](https://img.shields.io/pypi/pyversions/pyeurofx.svg?maxAge=2592000)](https://pypi.python.org/pypi/pyeurofx)

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

You can also get all the ISO currency codes and their names.

To use the module, do something like this - 

```python
import eurofx

daily = eurofx.get_daily_data()
historical = eurofx.get_historical_data()
currencies = eurofx.get_currency_list()

daily_df = eurofx.get_daily_data_df()
historical_df = eurofx.get_historical_data_df()
currencies_df_ = eurofx.get_currency_list_df_()

```

To see a ipython notebook example, visit - http://nbviewer.ipython.org/github/supercoderz/pyeurofx/blob/master/eurofx%20example.ipynb