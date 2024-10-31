import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(layout="wide", page_title="Best African Startups (3-Year Performance)")

st.title("Best African Startups (3-Year Performance)")

# Replace with actual African startup symbols and corresponding stock tickers.
# VERY IMPORTANT: These MUST be valid and publicly traded stock tickers.
african_startups = {
    "StartUpA": "YOUR_TICKER_A",  # Example - Replace with real tickers
    "StartUpB": "YOUR_TICKER_B",
    "StartUpC": "YOUR_TICKER_C",
    "StartUpD": "YOUR_TICKER_D",
    "StartUpE": "YOUR_TICKER_E"
}

# Sidebar for date input (fixed to 3 years)
st.sidebar.title("Input")
end_date = st.sidebar.date_input('End Date', value=datetime.date.today())
start_date = end_date - datetime.timedelta(days=3 * 365)  # 3 years prior


# Fetch data
startup_data = {}
for name, symbol in african_startups.items():
    try:
        startup_data[name] = yf.download(symbol, start=start_date, end=end_date)['Close']
    except Exception as e:
        st.warning(f"Could not retrieve data for {name} ({symbol}): {e}. Check ticker symbol and data availability.")

# Analysis and ranking (if data is available)
if startup_data:
    comparison_df = pd.DataFrame(startup_data)

    # Calculate total return over the period
    total_returns = (comparison_df.iloc[-1] / comparison_df.iloc[0]) - 1

    # Sort by total return
    ranked_startups = total_returns.sort_values(ascending=False)

    st.subheader("Ranked by 3-Year Total Return")
    st.write(ranked_startups)

    st.subheader("Closing Price Comparison")
    st.line_chart(comparison_df)
else:
    st.warning("No stock data available for comparison.")

st.sidebar.markdown("""
**Instructions:**

1. **Replace Placeholder Tickers:**  Use REAL stock tickers.  If the startups aren't public, this won't work.
2. **Data Availability:** Yahoo Finance data quality varies.  Double-check your tickers.
3. **Interpretation:** Total return is calculated as (Ending Price / Starting Price) - 1.
""")
