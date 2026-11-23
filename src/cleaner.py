import pandas as pd

def clean_data(df):
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(' ', '_') for c in df.columns]
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date']).drop_duplicates('date').sort_values('date')
    num_cols = [c for c in ['open', 'high', 'low', 'close', 'adj_close', 'volume'] if c in df.columns]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df[num_cols] = df[num_cols].ffill()          # fill gaps with last known value
    df = df.dropna(subset=['close'])
    return df.set_index('date')