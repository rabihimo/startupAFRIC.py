import streamlit as st
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd
# Removed the outer 'try...except' block as it was causing indentation issues
# and was likely unnecessary for the overall logic of the code

# African Startup Comparison
st.header("African Startup Stock Performance (Example)")
# Replace with actual African startup symbols
african_startups = {
    "StartUpA": "wave",  # Example - Replace with real tickers
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

