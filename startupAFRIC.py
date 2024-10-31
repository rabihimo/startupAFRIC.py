import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Global Startup Ranking")
st.title("Top Performing Global Startups (3-Year Analysis)")

# ... (rest of the code for data retrieval and ranking remains the same) ...

# Rank startups by 3-year return
if startup_data:
    ranked_startups = sorted(startup_data.items(), key=lambda item: item[1], reverse=True)
    
    # Create DataFrame for table and graph
    df_ranked = pd.DataFrame(ranked_startups, columns=['Startup', '3-Year Return'])
    df_ranked['Rank'] = df_ranked['3-Year Return'].rank(ascending=False, method='dense').astype(int)
    df_ranked = df_ranked[['Rank', 'Startup', '3-Year Return']]  # Reorder columns
    
    # --- Display Table ---
    st.subheader("Ranking Table:")
    st.table(df_ranked.style.format({'3-Year Return': '{:.2f}%'}))  # Format return as percentage

    # --- Display Graph (using matplotlib.pyplot) ---
    st.subheader("3-Year Return Bar Chart:")
    fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size if needed
    ax.bar(df_ranked['Startup'], df_ranked['3-Year Return'])
    ax.set_xlabel("Startup")
    ax.set_ylabel("3-Year Return (%)")
    ax.set_title("Top Performing Global Startups (3-Year Return)")
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    st.pyplot(fig)  # Display the matplotlib figure

else:
    st.warning("No sufficient data available for ranking.")
