from src.data_loader import get_stock_data
from src.cleaner import clean_data

raw, source = get_stock_data('AAPL', '2022-01-01')
df = clean_data(raw)

print('Shape:', df.shape)
print('Date range:', df.index.min().date(), 'to', df.index.max().date())
print('\n--- info ---')
df.info()
print('\n--- describe ---')
print(df[['open', 'high', 'low', 'close', 'volume']].describe().round(2))
print('\nHighest close:', df['close'].max().round(2), 'on', df['close'].idxmax().date())
print('Lowest close :', df['close'].min().round(2), 'on', df['close'].idxmin().date())
print('Average volume:', int(df['volume'].mean()))