import numpy as np
import pandas as pd

def make_sample(path='data/sample_stock.csv', days=750, seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end=pd.Timestamp.today().normalize(), periods=days)
    close = 100 * np.exp(np.cumsum(rng.normal(0.0004, 0.015, days)))
    df = pd.DataFrame({
        'Date': dates,
        'Open': close * (1 + rng.normal(0, 0.003, days)),
        'High': close * 1.01,
        'Low': close * 0.99,
        'Close': close,
        'Adj Close': close,
        'Volume': rng.integers(1_000_000, 5_000_000, days),
    })
    df.to_csv(path, index=False)
    print(f'Sample data saved to {path} (synthetic, for demo only)')

if __name__ == '__main__':
    make_sample()