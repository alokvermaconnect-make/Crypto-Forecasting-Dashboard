# 📈 Crypto Forecasting Dashboard
An end-to-end Machine Learning application that provides real-time price tracking and predictive analytics for Bitcoin (BTC) and Ethereum (ETH) using LSTM neural networks.

---

## 🚀 Overview
This project bridges the gap between raw financial data and actionable insights. By integrating live market data via the **Binance API**, the dashboard visualizes historical trends and uses a trained **Long Short-Term Memory (LSTM)** model to forecast future price movements.

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/) (Interactive Dashboard)
- **Language**: Python 3.x
- **Deep Learning**: TensorFlow / Keras (LSTM Model)
- **Data Handling**: Pandas, NumPy
- **Data Source**: Binance API / CoinGecko
- **Deployment**: GitHub & Streamlit Cloud

## 📊 Key Features
- **Live Price Tracking**: Real-time data fetching for top cryptocurrencies.
- **Time-Series Forecasting**: Predictive modeling using LSTM to handle sequence-based financial data.
- **Interactive Visualizations**: Dynamic charts showing historical vs. predicted prices.
- **Responsive UI**: Designed for seamless use across desktop and mobile.

## 📁 Project Structure
```text
├── data/               # Local datasets & pre-processing scripts
├── models/             # Saved LSTM models (.h5 or .pkl)
├── notebooks/          # Exploratory Data Analysis (EDA) & Model Training
├── src/                # Core logic for API integration
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
