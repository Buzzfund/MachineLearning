import numpy as np 
import pandas as pd 

# I trust all Buzzfund associates to not distribute this key
AlphaVantageKey = "DEMO"

# Fetch data for given ticker
def importData(ticker):
    daily_data = pd.read_csv("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&apikey="+AlphaVantageKey+"&datatype=csv", header = 0) 
    weekly_data = pd.read_csv("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol="+ticker+"&apikey="+AlphaVantageKey+"&datatype=csv", header = 0)
    
    return daily_data

# Get list of tickers we care about
def getTechTickers():
    tickers = pd.read_csv("./TechTickers.csv", header = None)
    return tickers

def main():
    tickers = getTechTickers()
    for index, row in tickers.iterrows():
        name = row[0]
        print("Fetching data for " + name)
        data = importData(name)
        print(data)



if __name__=="__main__": 
    main()