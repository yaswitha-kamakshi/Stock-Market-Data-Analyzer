import streamlit as st
from src.data_loader import get_stock_data
from src.cleaner import clean_data
from src.analysis import add_indicators, summarize

st.title('Stock Market Data Analyzer')
st.caption('Educational project, not financial advice.')
ticker = st.sidebar.text_input('Ticker', 'AAPL').upper()
start = st.sidebar.date_input('Start date', value=None)
start = str(start) if start else '2022-01-01'

if st.sidebar.button('Analyze'):
    raw, source = get_stock_data(ticker, start)
    df = add_indicators(clean_data(raw))
    s = summarize(df, ticker)
    st.write(f'Source: {source}')
    c1, c2, c3 = st.columns(3)
    c1.metric('Total return', f"{s['total_return_pct']:.1f}%")
    c2.metric('Volatility', f"{s['annualized_volatility_pct']:.1f}%")
    c3.metric('Max drawdown', f"{s['max_drawdown_pct']:.1f}%")
    st.subheader('Price and moving averages')
    st.line_chart(df[['close', 'sma_20', 'sma_50', 'sma_200']])
    st.subheader('Drawdown')
    st.area_chart(df['drawdown'])
    st.subheader('Summary'); st.json({k: str(v) for k, v in s.items()})