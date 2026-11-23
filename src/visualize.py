import matplotlib
matplotlib.use('Agg')   # save files without opening windows
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid')

def _save(fig, path):
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)

def plot_price(df, ticker, out='images'):
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(df.index, df['close'], label='Close', color='steelblue')
    ax.set(title=f'{ticker} Closing Price', xlabel='Date', ylabel='Price')
    ax.legend(); _save(fig, f'{out}/{ticker}_price.png')

def plot_moving_averages(df, ticker, out='images'):
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(df.index, df['close'], label='Close', alpha=0.5)
    for col in ('sma_20', 'sma_50', 'sma_200'):
        ax.plot(df.index, df[col], label=col.upper())
    ax.set(title=f'{ticker} Moving Averages', xlabel='Date', ylabel='Price')
    ax.legend(); _save(fig, f'{out}/{ticker}_moving_averages.png')

def plot_returns(df, ticker, out='images'):
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.histplot(df['daily_return'].dropna() * 100, bins=50, kde=True, ax=ax)
    ax.set(title=f'{ticker} Daily Return Distribution', xlabel='Daily return (%)')
    _save(fig, f'{out}/{ticker}_returns.png')

def plot_drawdown(df, ticker, out='images'):
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.fill_between(df.index, df['drawdown'] * 100, 0, color='crimson', alpha=0.4)
    ax.set(title=f'{ticker} Drawdown from Peak', xlabel='Date', ylabel='Drawdown (%)')
    _save(fig, f'{out}/{ticker}_drawdown.png')