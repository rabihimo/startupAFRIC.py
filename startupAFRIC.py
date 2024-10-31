# prompt: give me code to class the best african startups

import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(layout="wide", page_title="African Startup Comparison")

st.title("African Startup Stock Performance")

# Placeholder for actual African startup stock symbols
# Replace these with the appropriate symbols for your analysis
african_startups = {
    "StartUpA": "STKA", #Example Replace with real tickers.
    "StartUpB": "STKB", #Example Replace with real tickers.
    "StartUpC": "STKC", #Example Replace with real tickers.
    "StartUpD": "STKD", #Example Replace with real tickers.
    "StartUpE": "STKE"  #Example Replace with real tickers.
}


# Sidebar with date input
st.sidebar.title("Input")

col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date', value=datetime.date(2023, 1, 1))
with col2:
    edate = st.date_input('End Date', value=datetime.date.today())

# Fetch data for each selected startup
startup_data = {}
for name, symbol in african_startups.items():
    try:
        startup_data[name] = yf.download(symbol, start=sdate, end=edate)['Close']
    except Exception as e:
        st.warning(f"Could not retrieve data for {name} ({symbol}): {e}")

# Display charts only if data was successfully retrieved for at least one startup
if startup_data:
    comparison_df = pd.DataFrame(startup_data)
    st.line_chart(comparison_df)

    # Calculate daily percentage change
    daily_returns = comparison_df.pct_change() * 100
    st.line_chart(daily_returns)
else:
    st.warning("No stock data available for comparison.")
