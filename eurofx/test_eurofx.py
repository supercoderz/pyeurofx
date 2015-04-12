from .eurofx import *
from .eurofx_pandas import *

def test_get_daily():
	#just call this function which covers all
	get_daily_data()
	
def test_get_historical():
	#just call this function which covers all
	get_historical_data()
	
def test_get_daily_df():
	#just call this function which covers all
	get_daily_data_df()
	
def test_get_historical_df():
	#just call this function which covers all
	get_historical_data_df()

def test_get_currency_list_df():
    get_currency_list_df()

def test_get_currency_list():
    get_currency_list()