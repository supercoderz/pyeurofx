pyeurofx
=============

This is a simple module that fetches the daily and historical FX rates from ECB and parses the data.
The data is downloaded as XML files and returned as a list of (symbol, date, rate) tuples.

Install this module using 'pip install pyeurofx'

To use the module, do something like this - 

import eurofx

#last close price updated at 3 PM CET
daily = get_daily_data()

#all daily close prices from 1 Jan 1999
historical = get_historical_data()
