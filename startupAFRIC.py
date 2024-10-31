import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(layout="wide", page_title="Global Startup Ranking")
st.title("Top Performing Global Startups (3-Year Analysis)")

# Replace with actual global startup stock symbols
global_startups = {
    "Airbnb": "ABNB",
    "Snowflake": "SNOW",
    "DoorDash": "DASH",
    "UiPath": "PATH",
    "Affirm": "AFRM",
    # Add more startups here...
}

# Set analysis period (3 years)
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=3 * 365)  # Approx. 3 years

# Fetch and analyze data
startup_data = {}
for name, symbol in global_startups.items():
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        if not data.empty:
            # Calculate 3-year return (simple percentage change)
            three_year_return = (data['Close'][-1] - data['Close'][0]) / data['Close'][0] * 100
            startup_data[name] = three_year_return
        else:
            st.warning(f"No data found for {name} ({symbol}) within the 3-year period.")
    except Exception as e:
        st.warning(f"Could not retrieve data for {name} ({symbol}): {e}")

# Rank startups by 3-year return
if startup_data:
    ranked_startups = sorted(startup_data.items(), key=lambda item: item[1], reverse=True)
    
    st.subheader("Ranking Based on 3-Year Return:")
    for i, (name, return_value) in enumerate(ranked_startups):
        st.write(f"{i + 1}. {name}: {return_value:.2f}%")
    
    # Create a bar chart for visualization
    df_ranked = pd.DataFrame(ranked_startups, columns=['Startup', '3-Year Return'])
    st.bar_chart(df_ranked, x='Startup', y='3-Year Return')

else:
    st.warning("No sufficient data available for ranking.")
