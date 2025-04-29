import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Streamlit Page Settings ---
st.set_page_config(page_title="AI Stock Dashboard", layout="wide")
st.title("📈 AI-Powered Technical Analysis Dashboard")

# --- Sidebar ---
st.sidebar.header("Stock Settings")
ticker = st.sidebar.text_input("Enter Stock Symbol (example: AAPL)", value="AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2023-01-01'))
end_date = st.sidebar.date_input("End Date", pd.to_datetime('today'))

# --- Fetch Data ---
data = yf.download(ticker, start=start_date, end=end_date)

# --- Show Data ---
st.subheader(f"Stock Data for {ticker}")
st.dataframe(data.tail())

# --- Plot Closing Price ---
st.subheader("Closing Price Over Time")
fig, ax = plt.subplots()
ax.plot(data.index, data['Close'], label='Close Price', color='blue')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()
st.pyplot(fig)

