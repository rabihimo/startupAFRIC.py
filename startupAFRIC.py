import streamlit as st
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd

# Specify title and logo for the webpage.
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input")
symbol = st.sidebar.text_input('Please enter the stock symbol: ', 'NVDA').upper()

col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date', value=datetime.date(2024, 1, 1))
with col2:
    edate = st.date_input('End Date', value=datetime.date.today())

st.title(f"{symbol}")

try:
    stock = yf.Ticker(symbol)
    st.write(f"# Sector : {stock.info['sector']}")
    st.write(f"# Company Beta : {stock.info['beta']}")

    data = yf.download(symbol, start=sdate, end=edate)
    if data.empty:
        st.error(f"No data found for symbol '{symbol}' within the specified date range.")
    else:
        st.line_chart(data['Close'], x_label="Date", y_label="Close")

    # S&P 500 comparison
    st.header("S&P 500 Top 5 Comparison")
    top_5_symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA']  # Example, replace with dynamic data

    top_5_data = {}
    for sym in top_5_symbols:
        try:
            top_5_data[sym] = yf.download(sym, start=sdate, end=edate)['Close']
        except Exception as e:
            st.warning(f"Could not retrieve data for {sym}: {e}")

    if top_5_data:
        comparison_df = pd.DataFrame(top_5_data)
        st.line_chart(comparison_df)
    else:
        st.warning("Could not retrieve data for the S&P 500 top 5 comparison.")

    # Daily Percentage Change for Top 5
    st.header("S&P 500 Top 5 Comparison (Day-by-Day Fluctuation)")
    if top_5_data:
        comparison_df = pd.DataFrame(top_5_data)
        daily_returns = comparison_df.pct_change() * 100
        st.line_chart(daily_returns)
    else:
        st.warning("Could not retrieve data for the S&P 500 top 5 daily percentage change.")


    # African Startup Comparison
    st.header("African Startup Stock Performance (Example)")
    # Replace with actual African startup symbols
    african_startups = {
        "StartUpA": "STKA",  # Example - Replace with real tickers
        "StartUpB": "STKB",
        "StartUpC": "STKC",
        "StartUpD": "STKD",
        "StartUpE": "STKE"
    }

    startup_data = {}
    for name, symbol in african_startups.items():
        try:
            startup_data[name] = yf.download(symbol, start=sdate, end=edate)['Close']
        except Exception as e:
            st.warning(f"Could not retrieve data for {name} ({symbol}): {e}")

    if startup_data:
        comparison_df = pd.DataFrame(startup_data)
        st.line_chart(comparison_df)
        daily_returns = comparison_df.pct_change() * 100
        st.line_chart(daily_returns)
    else:
        st.warning("No stock data available for African startup comparison.")


    # Gold Price Fluctuations
    st.header("Gold Price Fluctuations in the US Market")
    gold_ticker = "GC=F"  # Gold Futures
    try:
      gold_data = yf.download(gold_ticker, start=sdate, end=edate)
      if not gold_data.empty:
          st.subheader("Gold Price (Close)")
          st.line_chart(gold_data["Close"])
          st.subheader("Daily Percentage Change")
          daily_returns = gold_data["Close"].pct_change() * 100
          st.line_chart(daily_returns)
      else:
          st.warning("No gold price data available.")
    except Exception as e:
      st.error(f"Error fetching gold data: {e}")


except Exception as e:
    st.error(f"An error occurred: {e}")
