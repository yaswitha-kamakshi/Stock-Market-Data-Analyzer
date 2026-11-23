import pandas as pd
import yfinance as yf

def fetch_from_yahoo(ticker, start, end=None):
    df = yf.download(ticker, start=start, end=end, auto_adjust=False, progress=False)
    if df.empty:
        raise ValueError(f'No data returned for {ticker}')
    if isinstance(df.columns, pd.MultiIndex):   # newer yfinance versions
        df.columns = df.columns.get_level_values(0)
    return df.reset_index()

def load_from_csv(path):
    return pd.read_csv(path)

def get_stock_data(ticker, start, end=None, csv_path='data/sample_stock.csv'):
    '''Try Yahoo Finance first, fall back to a local CSV.'''
    try:
        df = fetch_from_yahoo(ticker, start, end)
        source = 'Yahoo Finance'
        df.to_csv(f'data/{ticker}_raw.csv', index=False)
    except Exception as e:
        print(f'[WARN] Yahoo fetch failed ({e}). Using CSV fallback: {csv_path}')
        df = load_from_csv(csv_path)
        source = 'CSV fallback (sample data)'
    return df, source