import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from config import ALPHA_VANTAGE_API_KEY

# Dictionary of common stock symbols and their company names
COMMON_STOCKS = {
    "AAPL": "Apple Inc.",
    "GOOGL": "Alphabet Inc. (Google)",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com Inc.",
    "TSLA": "Tesla Inc.",
    "FB": "Meta Platforms Inc. (Facebook)",
    "NVDA": "NVIDIA Corporation",
    "JPM": "JPMorgan Chase & Co.",
    "V": "Visa Inc.",
    "JNJ": "Johnson & Johnson"
}

# Function to fetch live exchange rate
def get_live_exchange_rate():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data["rates"]["INR"]  # Get the INR exchange rate
        else:
            st.error("Error fetching exchange rates. Using default rate.")
            return 82.5  # Fallback default conversion rate
    except Exception as e:
        st.error(f"Error: {e}")
        return 82.5  # Fallback default conversion rate

def display_stock_market_data():
    st.header("Stock Market Data")
    
    # Fetch the live exchange rate for USD to INR
    conversion_rate = get_live_exchange_rate()
    st.write(f"Current Exchange Rate (1 USD to INR): ₹{conversion_rate:.2f}")

    # Currency selection
    currency = st.radio("Select Currency:", ["USD ($)", "INR (₹)"])
    
    # Stock symbol input
    col1, col2 = st.columns([2, 1])
    
    with col1:
        stock_symbol = st.text_input("Enter Stock Symbol:", value='AAPL')
    
    with col2:
        suggested_symbol = st.selectbox("Or choose a common stock:", 
                                        options=list(COMMON_STOCKS.keys()),
                                        format_func=lambda x: f"{x} - {COMMON_STOCKS[x]}")
    
    # Use the suggested symbol if it's changed, otherwise use the manually entered symbol
    if suggested_symbol != "AAPL":  # Default value in the selectbox
        stock_symbol = suggested_symbol
    
    if st.button("Get Stock Data"):
        stock_data = fetch_stock_data(stock_symbol)
        
        if stock_data is not None:
            st.subheader(f"Latest Stock Data for {stock_symbol} ({COMMON_STOCKS.get(stock_symbol, 'Unknown Company')})")
            
            # Convert prices to INR if selected
            if currency == "INR (₹)":
                stock_data[['Open', 'High', 'Low', 'Close']] *= conversion_rate
            
            st.write(stock_data.head())
            
            # Plotting the latest closing prices
            st.subheader("Closing Price Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(stock_data.index[:10], stock_data['Close'][:10], marker='o')
            ax.set_title(f'Closing Prices for {stock_symbol}')
            ax.set_xlabel('Time')
            ax.set_ylabel(f'Price ({currency})')
            plt.xticks(rotation=45)
            plt.grid()
            st.pyplot(fig)

        # Display additional stock information
        display_additional_stock_info(stock_data, stock_symbol, conversion_rate, currency)

def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact'
    response = requests.get(url)
    data = response.json()
    
    if 'Time Series (1min)' not in data:
        st.error("Failed to fetch data. Please check the stock symbol and try again.")
        return None
    
    df = pd.DataFrame.from_dict(data['Time Series (1min)'], orient='index')
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df.astype(float)
    return df

def display_additional_stock_info(stock_data, stock_symbol, conversion_rate, currency):
    if stock_data is not None and not stock_data.empty:
        st.subheader(f"Additional Information for {stock_symbol}")
        
        # Calculate daily change
        latest_close = stock_data['Close'].iloc[0]
        previous_close = stock_data['Close'].iloc[1]
        daily_change = (latest_close - previous_close) / previous_close * 100

        # Calculate trading volume
        total_volume = stock_data['Volume'].sum()

        # Display information
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Latest Close", f"{currency} {latest_close:.2f}")
        with col2:
            st.metric("Daily Change", f"{daily_change:.2f}%")
        with col3:
            st.metric("Trading Volume", f"{total_volume:,}")

        # Display moving averages
        st.subheader("Moving Averages")
        ma_5 = stock_data['Close'].rolling(window=5).mean()
        ma_20 = stock_data['Close'].rolling(window=20).mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(stock_data.index, stock_data['Close'], label='Close Price')
        ax.plot(ma_5.index, ma_5, label='5-day MA')
        ax.plot(ma_20.index, ma_20, label='20-day MA')
        ax.set_title(f'Moving Averages for {stock_symbol}')
        ax.set_xlabel('Time')
        ax.set_ylabel(f'Price ({currency})')
        ax.legend()
        plt.xticks(rotation=45)
        plt.grid()
        st.pyplot(fig)

        # Display price distribution
        st.subheader("Price Distribution")
        fig, ax = plt.subplots(figsize=(10, 5))
        stock_data['Close'].hist(bins=20, ax=ax)
        ax.set_title(f'Price Distribution for {stock_symbol}')
        ax.set_xlabel(f'Price ({currency})')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

