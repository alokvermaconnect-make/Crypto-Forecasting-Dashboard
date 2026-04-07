# 📈 Crypto Forecasting Dashboard

> Real-time cryptocurrency price forecasting with interactive trend visualisation. Async API integration with local cache fallback. Built and shipped production-ready at Amdox Technologies.

---

## 📌 What It Does

Fetches live cryptocurrency price data, applies time-series preprocessing, and renders interactive forecasting charts — all with a resilient async data pipeline that stays stable even when market APIs are volatile or rate-limited.

---

## ⚡ Key Features

| Feature | Detail |
|---|---|
| **Live Data Feeds** | Async fetch from crypto price APIs |
| **Cache Fallback** | Local cache layer keeps dashboard stable under API downtime |
| **Time-Series Preprocessing** | Normalisation + lag feature engineering |
| **Interactive Visualisation** | Multi-asset trend charts with zoom/filter |
| **Production Delivery** | Shipped within a 3-month internship cycle at Amdox Technologies |

---

## 🏗 Architecture

```
Live Crypto API
      │
      ▼
[Async Fetch Layer]
      │
   ┌──┴──┐
   │     │
Fresh  Cache Fallback
Data   (if API fails)
   │     │
   └──┬──┘
      │
[Time-Series Preprocessor]
  - Normalisation
  - Lag feature generation
  - Rolling averages
      │
      ▼
[Interactive Dashboard]
  - Multi-asset charts
  - Trend visualisation
  - Forecasting overlay
```

---

## 🛠 Tech Stack

- **Data Pipeline:** Python, asyncio, requests
- **Preprocessing:** Pandas, NumPy (normalisation, lag features)
- **Visualisation:** Streamlit / Plotly
- **Caching:** Local JSON/pickle cache with TTL logic
- **Deployment:** Streamlit Community Cloud

---

## 🚀 Run Locally

```bash
# Clone
git clone https://github.com/alokvermaconnect-make/Crypto-Forecasting-Dashboard.git
cd Crypto-Forecasting-Dashboard

# Install
pip install -r requirements.txt

# Run
streamlit run app.py
```

---

## 💡 Engineering Notes

**Why async fetch?**
Crypto APIs are notoriously rate-limited. A synchronous fetch blocks the entire dashboard during API slowdowns. Async + local cache means users always see data — even if the upstream API is down.

**Why lag features?**
Simple price plots are visually interesting but not analytically useful. Lag features (t-1, t-7, t-30 price) surface autocorrelation patterns that naive charts hide.

---

*Built at Amdox Technologies · Part of [Alok Verma's](https://alokvermaconnect-make.github.io/alok-verma-portfolio/) project portfolio.*
