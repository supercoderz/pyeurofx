import requests
from lxml import etree
import datetime


HISTORICAL='https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.xml'
DAILY='https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

def get_and_parse(data_url):
    result = requests.get(data_url)
    if result.status_code == requests.codes.ok:
        return parse_and_load(result.content)
        
def parse_and_load(content):
    data = []
    doc = etree.XML(content)
    nodes = doc.iterchildren()
    subject = nodes.__next__()
    sender = nodes.__next__()
    parent_cube = nodes.__next__()
    for daily_cube in parent_cube.iterchildren():
        time = daily_cube.attrib['time']
        for currency_cube in daily_cube.iterchildren():
            currency = currency_cube.attrib['currency']
            rate = currency_cube.attrib['rate']
            date = get_date(time)
            data.append((currency,date,rate))
    return data
                
def get_date(date_string):
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
