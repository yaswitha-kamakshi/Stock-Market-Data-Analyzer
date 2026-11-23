from datetime import datetime

def write_report(s, source, out='reports'):
    path = f"{out}/{s['ticker']}_report.md"
    text = f'''# {s['ticker']} Analysis Report
Generated: {datetime.now():%Y-%m-%d %H:%M} | Data source: {source}

## Period
{s['start']} to {s['end']} ({s['trading_days']} trading days)

## Price Summary
- Highest close: {s['highest_close']:.2f} on {s['highest_date']}
- Lowest close: {s['lowest_close']:.2f} on {s['lowest_date']}
- Total return: {s['total_return_pct']:.2f}%
- Annualized return: {s['annualized_return_pct']:.2f}%
- Average daily return: {s['avg_daily_return_pct']:.3f}%
- Best day: {s['best_day']}
- Worst day: {s['worst_day']}

## Risk Summary
- Annualized volatility: {s['annualized_volatility_pct']:.2f}% ({s['risk_level']} risk)
- Maximum drawdown: {s['max_drawdown_pct']:.2f}%
- Sharpe ratio (rf=0): {s['sharpe_ratio']:.2f}

## Trend
{s['trend']}

*Disclaimer: educational project, not financial advice.*
'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    return path