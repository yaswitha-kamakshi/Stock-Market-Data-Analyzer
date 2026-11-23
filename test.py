from src.data_loader import get_stock_data
from src.cleaner import clean_data
from src.analysis import add_indicators
from src import visualize as viz

raw, source = get_stock_data('AAPL', '2022-01-01')
df = add_indicators(clean_data(raw))

viz.plot_price(df, 'AAPL')
viz.plot_moving_averages(df, 'AAPL')
viz.plot_returns(df, 'AAPL')
viz.plot_drawdown(df, 'AAPL')
print('Charts saved in images/')