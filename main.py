import argparse, os
from src.data_loader import get_stock_data
from src.cleaner import clean_data
from src.analysis import add_indicators, summarize
from src import visualize as viz
from src.report import write_report

def run(ticker, start, end):
    for d in ('data', 'outputs', 'images', 'reports'):
        os.makedirs(d, exist_ok=True)
    raw, source = get_stock_data(ticker, start, end)
    print(f'Data source: {source}\nRaw shape: {raw.shape}')
    df = add_indicators(clean_data(raw))
    print(df[['close', 'daily_return', 'sma_50', 'volatility_30d']].tail())
    df.to_csv(f'outputs/{ticker}_processed.csv')
    s = summarize(df, ticker)
    viz.plot_price(df, ticker); viz.plot_moving_averages(df, ticker)
    viz.plot_returns(df, ticker); viz.plot_drawdown(df, ticker)
    path = write_report(s, source)
    print(f'\nReport saved: {path}')
    for k, v in s.items():
        print(f'{k:28}: {v}')
    return df, s, source

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Stock Market Data Analyzer')
    p.add_argument('--ticker', default='AAPL')
    p.add_argument('--start', default='2022-01-01')
    p.add_argument('--end', default=None)
    a = p.parse_args()
    run(a.ticker.upper(), a.start, a.end)