from src.data_loader import get_stock_data
from src.cleaner import clean_data
from src.analysis import add_indicators

raw, source = get_stock_data('AAPL', '2022-01-01')
df = add_indicators(clean_data(raw))

print(df[['close', 'sma_20', 'sma_50', 'sma_200']].head(3))
print('\nLast 5 rows:')
print(df[['close', 'sma_20', 'sma_50', 'sma_200']].tail().round(2))
print('\nNaN in sma_200:', df['sma_200'].isnull().sum())

last = df.iloc[-1]
print('\nPrice above SMA50?', last['close'] > last['sma_50'])
print('SMA50 above SMA200?', last['sma_50'] > last['sma_200'])