import seaborn
import numpy as np
import pandas as pd
from datetime import datetime
import pandas_datareader.data as web  ### FRED API
import pandas_datareader.wb as wb     ### World Bank API

gold_prices = pd.read_csv('gold_prices.csv')
#print(gold_prices)
crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
#print(crude_oil_prices)

start=datetime(1999,1,1)
end=datetime(2019,1,1)

nasdaq_data = web.DataReader('NASDAQ100','fred',start,end)
#print(nasdaq_data)
#print(len(nasdaq_data))

sap_data = web.DataReader('SP500','fred',start,end)
#print(sap_data)
#print(len(sap_data))


gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)
#print(gdp_data)

export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)
#print(export_data)


def log_return(prices):
  return np.log(prices/prices.shift(1))

gold_returns = log_return(gold_prices['Gold_Price'])
crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])
sap_returns = log_return(sap_data['SP500'])
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])

print(gold_returns.var())
print(crude_oil_returns.var())
print(nasdaq_returns.var())
print(sap_returns.var())
print(gdp_returns.var())
print(export_returns.var())

