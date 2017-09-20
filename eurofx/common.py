import requests
from lxml import etree
import datetime
import pandas
import tempfile
import zipfile
import uuid
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO as IO
else:
    from io import BytesIO as IO

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
        return parse_and_load_csv(data,use_pandas,data_url==DAILY)
        
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


def parse_and_load_csv(content,use_pandas,is_daily):
    result=[]
    d=IO(content)
    df=pandas.read_csv(d)
    df['Date']=df.apply(lambda r:get_date(r['Date']),axis=1)
    df=df.set_index(['Date'])
    if " " in df.columns:
        df=df.drop([" "],axis=1)
    cols=df.columns
    cols=[c.strip() for c in cols]
    df.columns=cols
    if use_pandas:
        return df
    def get_tuple(x):
        date=x.name
        pairs=[(k.strip(),date,x[k]) for k in x.keys().tolist() if x[k]!=' ' and 'Unnamed' not in k]
        result.extend(pairs)
        return 1
    df['result']=df.apply(lambda x:get_tuple(x),axis=1)
    return result

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

def get_date(date_string):
    d=None
    try:
        d=datetime.datetime.strptime(date_string, "%d %B %Y").date()
    except:
        d=datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

    if d:
        return d.strftime("%Y-%m-%d")
    else:
        return date_string

