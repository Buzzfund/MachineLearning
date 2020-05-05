# https://financialmodelingprep.com/developer/docs
# Script for data collection
# Felix Hu
################################################################

import numpy as np
import pandas as pd
from urllib.request import urlopen
import json

columns = list() # hold key values in 'data', used to write to CSV file
data = dict() # hold historical data
currPrice = dict() # hold current pricing data, used for testing

def getTechTickers(file):
    tickers = pd.read_csv(file, header = None)
    ret = list()
    for index, row in tickers.iterrows():
        name = row[0]
        ret.append(name)
    return ret

def getJSONFrom(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def indexListByThree(arr):
    """
        return 'arr' split into sublists of length 3
        FinancialModelPrep only allows queres of 3 tickers at a time
    """
    ret = list()
    residual = len(arr) % 3
    for i in range(0, len(arr)-residual-1, 3):
        sublist = arr[i: i+3]
        ret.append(sublist)
    if residual != 0:
        ret.append(arr[len(arr)-residual:])
    return ret

def getSector(tickers):
    # Note: Financial Modeling Prep only allows 3 tickers at a time
    
    # update columns
    if "sector" not in columns:
        columns.append("sector")

    split_tickers = indexListByThree(tickers)

    ori_len = len(tickers)
    for i in range(0, len(split_tickers)):
        sublist = split_tickers[i]
        print("Index "+str(min(i*3, ori_len))+"/"+str(ori_len)+": "+str(sublist), end="\r")
        url = "https://financialmodelingprep.com/api/v3/company/profile/"
        url = url + ','.join(sublist)
        fetched_data = getJSONFrom(url)
        profiles = dict()
        if len(sublist) > 1: 
            profiles = fetched_data['companyProfiles']
        else:
            profiles = [fetched_data]
        #print(profiles)
        for i in range(0, len(profiles)):
            data[profiles[i]['symbol']]["sector"] = profiles[i]['profile']['sector']

def getHistoricalDailyPrice(tickers):

    split_tickers = indexListByThree(tickers)
    ori_len = len(tickers)
    for i in range(0, len(split_tickers)):
        sublist = split_tickers[i]
        print("Index "+str(min(i*3, ori_len))+"/"+str(ori_len)+": "+str(sublist), end="\r")
        url = "https://financialmodelingprep.com/api/v3/historical-price-full/"        
        url = url + ','.join(sublist)
        fetched_data = getJSONFrom(url)
        profiles = dict()
        if len(sublist) > 1: 
            profiles = fetched_data['companyProfiles']
        else:
            profiles = [fetched_data]
        #print(profiles)
        for i in range(0, len(profiles)):
            data[profiles[i]['symbol']]["sector"] = profiles[i]['profile']['sector']

def getRating(tickers):
    split_tickers = indexListByThree(tickers)
    ori_len = len(tickers)
    for i in range(0, len(split_tickers)):
        sublist = split_tickers[i]
        print("Index "+str(min(i*3, ori_len))+"/"+str(ori_len)+": "+str(sublist), end="\r")
        url = "https://financialmodelingprep.com/api/v3/historical-price-full/"        
        url = url + ','.join(sublist)
        fetched_data = getJSONFrom(url)
        profiles = dict()
        if len(sublist) > 1: 
            profiles = fetched_data['companyProfiles']
        else:
            profiles = [fetched_data]
        #print(profiles)
        for i in range(0, len(profiles)):
            data[profiles[i]['symbol']]["sector"] = profiles[i]['profile']['sector']

def getCurrPrice(tickers):
    url = "https://financialmodelingprep.com/api/v3/stock/real-time-price/"
    url = url + ",".join(tickers)
    data = getJSONFrom(url)['companiesPriceList']
    for entry in data:
        currPrice[entry['symbol']] = entry['price']


def main():
    print("Fetching ticker names...")
    tickers = getTechTickers("./SP500.csv")

    print("Creating ticker entries in dictionary...")
    for ticker in tickers:
        data[ticker] = dict()

    print("Fetching ticker sectors...")
    #getSector(tickers)

    #getCurrPrice(tickers)

    #print(indexListByThree(tickers))

    #print(data)

        
        

if __name__=="__main__": 
    main()