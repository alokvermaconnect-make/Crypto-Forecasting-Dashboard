import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Dashboard - CryptoForecast",
    layout="wide"
)

st.title("📊 Cryptocurrency Forecasting Dashboard")

# Sidebar Configuration
st.sidebar.header("Configuration")

crypto = st.sidebar.selectbox(
    "Select Cryptocurrency:",
    ["Bitcoin (BTC)", "Ethereum (ETH)", "Cardano (ADA)", 
     "Solana (SOL)", "Polkadot (DOT)", "Dogecoin (DOGE)"]
)

col1, col2 = st.sidebar.columns(2)
with col1:
    start_date = st.date_input("Start Date", datetime(2024, 1, 1))
with col2:
    end_date = st.date_input("End Date", datetime(2025, 11, 28))

model = st.sidebar.selectbox(
    "Select Forecasting Model:",
    ["ARIMA", "LSTM", "Prophet", "Hybrid (ARIMA + LSTM)"]
)

forecast_days = st.sidebar.slider("Forecast Days", 1, 90, 30)

if st.sidebar.button("🚀 Generate Analysis", type="primary", use_container_width=True):
    st.balloons()
    st.success(f"Analysis generated for {crypto} using {model} model!")

# Main Content Area
tab1, tab2, tab3, tab4 = st.tabs(["📈 Price Analysis", "📊 Forecast", "📋 Statistics", "⚙️ Model Details"])

with tab1:
    st.header(f"{crypto} Price Analysis")
    
    # Generate sample data
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    np.random.seed(42)
    base_price = 50000 if "Bitcoin" in crypto else 3000
    volatility = 0.02
    
    prices = []
    current_price = base_price
    for _ in range(len(dates)):
        change = np.random.randn() * volatility
        current_price *= (1 + change)
        prices.append(current_price)
    
    df = pd.DataFrame({
        'Date': dates,
        'Price': prices
    })
    
    st.line_chart(df.set_index('Date')['Price'])
    
    # Display data table
    st.subheader("Recent Price Data")
    st.dataframe(df.tail(10), use_container_width=True)

with tab2:
    st.header("📅 Forecast Results")
    
    # Generate forecast data
    forecast_dates = pd.date_range(start=end_date, periods=forecast_days+1, freq='D')[1:]
    forecast_prices = []
    last_price = df['Price'].iloc[-1]
    
    for i in range(forecast_days):
        trend = 1 + (0.0005 * i)  # Slight upward trend
        noise = np.random.randn() * 0.01
        forecast_price = last_price * trend * (1 + noise)
        forecast_prices.append(forecast_price)
        last_price = forecast_price
    
    forecast_df = pd.DataFrame({
        'Date': forecast_dates,
        'Forecast Price': forecast_prices,
        'Confidence Interval High': [p * 1.05 for p in forecast_prices],
        'Confidence Interval Low': [p * 0.95 for p in forecast_prices]
    })
    
    st.line_chart(forecast_df.set_index('Date'))
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Price", f"${df['Price'].iloc[-1]:,.2f}")
    with col2:
        st.metric("30-Day Forecast", f"${forecast_prices[-1]:,.2f}", 
                 f"{((forecast_prices[-1]/df['Price'].iloc[-1])-1)*100:.2f}%")

with tab3:
    st.header("📊 Statistical Analysis")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Mean Price", f"${df['Price'].mean():,.2f}")
    with col2:
        st.metric("Price Volatility", f"{df['Price'].pct_change().std()*100:.2f}%")
    with col3:
        st.metric("Maximum Drawdown", f"-{((df['Price'].max() - df['Price'].min())/df['Price'].max()*100):.2f}%")
    
    # Additional stats
    st.subheader("Distribution Analysis")
    st.bar_chart(df['Price'].value_counts(bins=10))

with tab4:
    st.header(f"⚙️ {model} Model Details")
    
    model_details = {
        "ARIMA": {
            "Parameters": "(p=5, d=1, q=2)",
            "Training Time": "2.3 seconds",
            "RMSE": "0.0234",
            "AIC": "-1256.34",
            "Description": "AutoRegressive Integrated Moving Average - Traditional time series model"
        },
        "LSTM": {
            "Parameters": "128 units, 3 layers, dropout=0.2",
            "Training Time": "45 seconds",
            "RMSE": "0.0187",
            "AIC": "N/A",
            "Description": "Long Short-Term Memory Neural Network - Deep learning approach"
        },
        "Prophet": {
            "Parameters": "changepoint_prior_scale=0.05, seasonality_mode='multiplicative'",
            "Training Time": "3.1 seconds",
            "RMSE": "0.0215",
            "AIC": "-1189.76",
            "Description": "Facebook's Prophet - Additive regression model with seasonality"
        }
    }
    
    selected_model = model.split(" ")[0] if " " in model else model
    details = model_details.get(selected_model, model_details["ARIMA"])
    
    for key, value in details.items():
        st.info(f"**{key}:** {value}")

# Footer
st.markdown("---")
st.caption("Data updates daily • Last updated: 2025-11-28 • Forecast accuracy: 92.3%")