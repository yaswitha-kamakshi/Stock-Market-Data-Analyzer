from src.data_loader import get_stock_data
from src.cleaner import clean_data
from src.analysis import add_indicators, summarize

raw, source = get_stock_data('AAPL', '2022-01-01')
df = add_indicators(clean_data(raw))

print(df[['close', 'daily_return', 'cumulative_return', 'volatility_30d', 'drawdown']].tail().round(4))

s = summarize(df, 'AAPL')
print()
for k, v in s.items():
    print(f'{k:28}: {v}')