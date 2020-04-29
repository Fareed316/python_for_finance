import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

# pandas_datareader replaces pandas.data.io

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)
# format is year month day

df = web.DataReader('TSLA','yahoo', start, end)

#Handling Data and Graphing
df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv',parse_dates=True, index_col = 0)

df.head()
df['Adj Close'].plot()
plt.show()
# df['Adj Close']
df[['Open','High']].head()