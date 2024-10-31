import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(layout="wide", page_title="African Startup Comparison")

st.title("African Startup Stock Performance (Example)")

# Replace with actual African startup symbols and corresponding stock tickers.  Crucially, these MUST be valid stock tickers.
# If the startups are not publicly traded, you will need to find alternative data sources.
african_startups = {
    "StartUpA": "Flutterwave",  # Example - Replace with real tickers
    "StartUpB": "Chipper Cash",
    "StartUpC": "Jumia",
    "StartUpD": "Andela",
    "StartUpE": "Paystack"
}


# Sidebar for date input
st.sidebar.title("Input")
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date', value=datetime.date(2021, 1, 1))  # Start date 3 years ago
with col2:
    edate = st.date_input('End Date', value=datetime.date.today())


# Fetch data for each selected startup
startup_data = {}
for name, symbol in african_startups.items():
    try:
        startup_data[name] = yf.download(symbol, start=sdate, end=edate)['Close']
    except Exception as e:
        st.warning(f"Could not retrieve data for {name} ({symbol}): {e}.  Please check if the ticker symbol is correct or if the company is publicly traded.")

# Display charts
if startup_data:
    comparison_df = pd.DataFrame(startup_data)

    # Display closing price chart
    st.subheader("Closing Price Comparison")
    st.line_chart(comparison_df)

    # Calculate and display daily percentage change
    st.subheader("Daily Percentage Change")
    daily_returns = comparison_df.pct_change() * 100
    st.line_chart(daily_returns)
else:
    st.warning("No stock data available for comparison. Check the provided tickers and ensure they are valid and data is available for the specified time period.")

