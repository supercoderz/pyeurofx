import requests
from lxml import etree
import datetime
import pandas
import tempfile
import zipfile
import uuid
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

HISTORICAL='https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip'
DAILY='https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'
ISO_CURRENCIES = 'http://www.currency-iso.org/dam/downloads/lists/list_one.xml'

def get_data_and_read_file(data_url):
    result = requests.get(data_url)
    if result.status_code == requests.codes.ok:
        tmpdir = tempfile.mkdtemp()
        fname = tmpdir+'/'+str(uuid.uuid1())
        with open(fname,'wb') as f:
            f.write(result.content)
        z = zipfile.ZipFile(fname)
        return z.read(z.namelist()[0])

def get_and_parse(data_url,use_pandas=False):
    data = get_data_and_read_file(data_url)
    if data:
        if use_pandas:
            return parse_and_load_df(data)
        else:
            return parse_and_load_csv(data)
        
def get_and_parse_currency_list(data_url,use_pandas=False):
    result = requests.get(data_url)
    if result.status_code == requests.codes.ok:
        currencies = parse_and_load_currency_list(result.content)
        if use_pandas:
            return get_currencies_df(currencies)
        return currencies

def get_currencies_df(data):
    df = pandas.DataFrame({'Code':[],'Name':[]})
    df = df.set_index('Code')
    for i in data:
        code,name = i
        df.ix[code] = name
    return df


def parse_and_load_csv(content):
    d=StringIO(content)
    df=pandas.read_csv(d)
    return df


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
            try:
                rate = float(currency_cube.attrib['rate'])
            except:
                rate = 1
            date = get_date(time)
            data.append((currency,date,rate))
    return data

def parse_and_load_currency_list(content):
    data = []
    doc = etree.XML(content)
    nodes = doc.iterchildren()
    ccy_tbl = nodes.__next__()
    for ccy_ntry in ccy_tbl.iterchildren():
        ccy_name = None
        ccy_code = None
        for child in ccy_ntry.iterchildren():
            if child.tag == 'Ccy':
                ccy_code = child.text
            elif child.tag == 'CcyNm':
                ccy_name = child.text
        if ccy_name and ccy_code:
            data.append((ccy_code,ccy_name))
    return data

def parse_and_load_df(content):
    data = []
    doc = etree.XML(content)
    nodes = doc.iterchildren()
    subject = nodes.__next__()
    sender = nodes.__next__()
    parent_cube = nodes.__next__()
    times,currencies = get_index_and_cols(parent_cube)
    df = pandas.DataFrame(index=times,columns=currencies,dtype=float)
    load_dataframe(df,parent_cube)
    return df
    

def load_dataframe(df,node):
    for daily_cube in node.iterchildren():
        time = daily_cube.attrib['time']
        for currency_cube in daily_cube.iterchildren():
            currency = currency_cube.attrib['currency']
            try:
                rate = float(currency_cube.attrib['rate'])
            except:
                rate = 1
            df.ix[time,currency] = rate

def get_index_and_cols(node):
    times = []
    currencies = []
    for daily_cube in node.iterchildren():
        time = daily_cube.attrib['time']
        times.append(time)
        for currency_cube in daily_cube.iterchildren():
            currency = currency_cube.attrib['currency']
            if currency not in currencies:
                currencies.append(currency)
    return (times,currencies)
                    
def get_date(date_string):
    try:
        return datetime.datetime.strptime(date_string, "%d %B %Y").date()
    except:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

