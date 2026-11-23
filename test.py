from src.data_loader import get_stock_data
df, source = get_stock_data('AAPL', '2022-01-01')
print(source)
print(df.head())
print(df.shape)