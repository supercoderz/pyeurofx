from .common import *

def get_historical_data():
    return get_and_parse(HISTORICAL)

def get_daily_data():
    return get_and_parse(DAILY)
