# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
#for dirname, _, filenames in os.walk('/kaggle/input'):
#    for filename in filenames:
#        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
#-----------------------------------------------------------------------------------------------------------

import math
import seaborn as sns
import datetime as dt
from datetime import datetime    
sns.set_style("whitegrid")
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use("ggplot")

data = pd.read_csv('../input/price-volume-data-for-all-us-stocks-etfs/Stocks/abe.us.txt')
#data = pd.read_csv('../input/nifty50-stock-market-data/COALINDIA.csv')
#data = pd.read_csv('../input/stock-market-data/stock_market_data/nasdaq/csv/ABCO.csv')
#data = pd.read_csv('./data.csv')
# Any CSV or TXT file can be added here....
data.head()
#-----------------------------------------------------------------------------------------------------------
plt.plot(data['Close'], label="Close price")
plt.xlabel("Timestamp")
plt.ylabel("Closing price")
df = data
print("data",df)

df.describe().transpose()

#-----------------------------------------------------------------------------------------------------------
data.reset_index(drop=True, inplace=True)
data.fillna(data.mean(), inplace=True)
data.head()

#------------------------------------------------------------------------------------------------------------
def plotAllprices():
  #creates EMA and plots open, close, EMA, and average prices
  data.plot(legend=True,subplots=True, figsize = (12, 6))
  plt.show()
  #data['Close'].plot(legend=True, figsize = (12, 6))
  #plt.show()
  #data['Volume'].plot(legend=True,figsize=(12,7))
  #plt.show()
  
  data.shape
  data.size
  data.describe(include='all').T
  data.dtypes
  data.nunique()
  ma_day = [10,50,100]
  for ma in ma_day:
      column_name = "MA for %s days" %(str(ma))
      data[column_name]=pd.DataFrame.rolling(data['Close'],ma).mean()
  
  data['Daily Return'] = data['Close'].pct_change()
  # plot the daily return percentage
  data['Daily Return'].plot(figsize=(12,5),legend=True,linestyle=':',marker='o')
  plt.show()
  
  sns.displot(data['Daily Return'].dropna(),bins=100,color='green')
  plt.show()
  
  date=pd.DataFrame(data['Date'])
  closing_df1 = pd.DataFrame(data['Close'])
  close1  = closing_df1.rename(columns={"Close": "data_close"})
  close2=pd.concat([date,close1],axis=1)
  close2.head()
  data.reset_index(drop=True, inplace=True)
  data.fillna(data.mean(), inplace=True)
  data.head()
  
  data.nunique()
  
  data.sort_index(axis=1,ascending=True)
  
  cols_plot = ['Open', 'High', 'Low','Close','Volume','MA for 10 days','MA for 50 days','MA for 100 days','Daily Return']
  axes = data[cols_plot].plot(marker='.', alpha=0.7, linestyle='None', figsize=(11, 9), subplots=True)
  for ax in axes:
      ax.set_ylabel('Daily trade')
  
  plt.plot(data['Close'], label="Close price")
  plt.xlabel("Timestamp")
  plt.ylabel("Closing price")
  df = data
  print(df[0])
  
  data.isnull().sum()


