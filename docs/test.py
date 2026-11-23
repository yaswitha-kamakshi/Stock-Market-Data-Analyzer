from src.data_loader import get_stock_data
from src.cleaner import clean_data

raw, source = get_stock_data('AAPL', '2022-01-01')
print('Source:', source)
print('RAW columns:', list(raw.columns))
print('RAW missing values:', raw.isnull().sum().sum())
print('RAW duplicate dates:', raw['Date'].duplicated().sum())

df = clean_data(raw)
print('\nCLEAN columns:', list(df.columns))
print('Index type:', type(df.index).__name__)
print('Missing after cleaning:', df.isnull().sum().sum())
print(df.head())