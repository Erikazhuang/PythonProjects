import requests
import json
import pandas as pd
import socketio
from sec_api import QueryApi


api_key = "f31a6c4efa00c34de0bc6cfc0571e675d952197274155eb9a639532fc8984eac"

def getLiveStream():
    sio = socketio.Client()
 
    @sio.on('connect', namespace='/all-filings')
    def on_connect():
        print("Connected to https://api.sec-api.io:3334/all-filings")
    
    @sio.on('filing', namespace='/all-filings')
    def on_filings(filing):
        print(filing)
    
    sio.connect('https://api.sec-api.io:3334?apiKey='+ api_key, namespaces=['/all-filings'], transports=["websocket"])
    sio.wait()



def getIncomeStatement():

    # 10-Q filing URL of Apple
    filing_url = "https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/aapl-20210925.htm"

    # XBRL-to-JSON converter API endpoint
    xbrl_converter_api_endpoint = "https://api.sec-api.io/xbrl-to-json"

    # get your API key at https://sec-api.io
   

    final_url = xbrl_converter_api_endpoint + "?htm-url=" + filing_url + "&token=" + api_key

    # make request to the API
    response = requests.get(final_url)

    # load JSON into memory
    xbrl_json = json.loads(response.text)

    # income statement example
    for eps in (xbrl_json['StatementsOfIncome']['EarningsPerShareBasic']):
        print(str(eps['period']) + ' ' + str(eps['value']))


def download10q(key):

    queryApi = QueryApi(key)

    query = {
    "query": { "query_string": { 
        "query": "ticker:AAPL AND filedAt:{2021-09-01 TO 2021-12-31} AND formType:\"10-Q\"" 
        } },
    "from": "0",
    "size": "10",
    "sort": [{ "filedAt": { "order": "desc" } }]
    }

    filings = queryApi.get_filings(query)

    print(filings)


getIncomeStatement()