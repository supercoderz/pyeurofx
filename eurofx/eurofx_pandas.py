from .common import *

def get_historical_data_df():
    return get_and_parse(HISTORICAL,use_pandas=True)

def get_daily_data_df():
    return get_and_parse(DAILY,use_pandas=True)
