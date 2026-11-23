import numpy as np

def add_indicators(df):
    df = df.copy()
    df['daily_return'] = df['close'].pct_change()
    df['cumulative_return'] = (1 + df['daily_return'].fillna(0)).cumprod() - 1
    for w in (20, 50, 200):
        df[f'sma_{w}'] = df['close'].rolling(w).mean()
    df['ema_20'] = df['close'].ewm(span=20, adjust=False).mean()
    df['volatility_30d'] = df['daily_return'].rolling(30).std() * np.sqrt(252)
    peak = df['close'].cummax()
    df['drawdown'] = df['close'] / peak - 1
    return df

def summarize(df, ticker):
    r = df['daily_return'].dropna()
    years = max((df.index[-1] - df.index[0]).days / 365.25, 1e-9)
    total = df['close'].iloc[-1] / df['close'].iloc[0] - 1
    last = df.iloc[-1]
    if last['close'] > last['sma_50'] > last['sma_200']:
        trend = 'Uptrend (price above SMA50 and SMA200)'
    elif last['close'] < last['sma_50'] < last['sma_200']:
        trend = 'Downtrend (price below SMA50 and SMA200)'
    else:
        trend = 'Sideways / mixed signals'
    vol = r.std() * np.sqrt(252)
    return {
        'ticker': ticker,
        'start': df.index[0].date(), 'end': df.index[-1].date(),
        'trading_days': len(df),
        'highest_close': df['close'].max(), 'highest_date': df['close'].idxmax().date(),
        'lowest_close': df['close'].min(), 'lowest_date': df['close'].idxmin().date(),
        'total_return_pct': total * 100,
        'annualized_return_pct': ((1 + total) ** (1 / years) - 1) * 100,
        'avg_daily_return_pct': r.mean() * 100,
        'annualized_volatility_pct': vol * 100,
        'sharpe_ratio': (r.mean() * 252) / (vol + 1e-9),   # risk-free rate assumed 0
        'max_drawdown_pct': df['drawdown'].min() * 100,
        'best_day': f"{r.idxmax().date()} ({r.max()*100:.2f}%)",
        'worst_day': f"{r.idxmin().date()} ({r.min()*100:.2f}%)",
        'trend': trend,
        'risk_level': 'High' if vol > 0.40 else 'Medium' if vol > 0.20 else 'Low',
    }