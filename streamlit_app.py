import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="CryptoForecast AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    /* Main styling */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #00d4ff, #0088ff, #00ff88);
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0, 212, 255, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Feature cards */
    .feature-card {
        background: rgba(30, 30, 60, 0.7);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #2a2a5a;
        transition: transform 0.3s, box-shadow 0.3s;
        backdrop-filter: blur(10px);
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.4);
        border-color: #00d4ff;
    }
    
    /* Navigation buttons */
    .nav-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
        margin: 10px 0;
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .nav-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.5);
    }
    
    /* Chart containers */
    .chart-box {
        background: rgba(20, 20, 40, 0.8);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #3a3a6a;
        margin: 1rem 0;
    }
    
    /* Metrics styling */
    .metric-box {
        background: rgba(0, 212, 255, 0.1);
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 5px solid #00d4ff;
        margin: 0.5rem 0;
    }
    
    /* Text styling */
    .crypto-text {
        background: linear-gradient(90deg, #00d4ff, #0088ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    
    /* Section headers */
    .section-header {
        border-left: 5px solid #00ff88;
        padding-left: 15px;
        margin: 2rem 0 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ====================
# MAIN HEADER SECTION
# ====================
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3.5rem; margin: 0; font-weight: 800;">🚀 CRYPTOFORECAST AI</h1>
    <p style="font-size: 1.5rem; margin: 1rem 0 0 0; opacity: 0.9;">Advanced Cryptocurrency Analytics & AI-Powered Forecasting Platform</p>
    <div style="margin-top: 1.5rem; display: flex; justify-content: center; gap: 20px;">
        <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px;">🤖 AI-Powered</span>
        <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px;">📊 Real-time Data</span>
        <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px;">📈 Predictive Analytics</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ====================
# NAVIGATION SECTION
# ====================
st.markdown('<h2 class="section-header">🚀 Quick Navigation</h2>', unsafe_allow_html=True)

nav_col1, nav_col2, nav_col3 = st.columns(3)

with nav_col1:
    if st.button("📊 **TRADING DASHBOARD**", use_container_width=True, type="primary"):
        st.switch_page("pages/1_🏠_Dashboard.py")

with nav_col2:
    if st.button("📖 **PLATFORM GUIDE**", use_container_width=True, type="secondary"):
        st.switch_page("pages/2_📋_Description.py")

with nav_col3:
    if st.button("👥 **OUR TEAM**", use_container_width=True, type="secondary"):
        st.switch_page("pages/3_👥_Team_Overview.py")

# ====================
# KEY FEATURES SECTION
# ====================
st.markdown('<h2 class="section-header">✨ Key Features & Capabilities</h2>', unsafe_allow_html=True)

# Features Grid
features_grid = st.columns(3)

with features_grid[0]:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #00d4ff;">🤖 AI Forecasting Models</h3>
        <p><strong>• ARIMA:</strong> Time-tested statistical model for stable predictions</p>
        <p><strong>• LSTM Neural Networks:</strong> Deep learning for complex patterns</p>
        <p><strong>• Prophet:</strong> Facebook's model for seasonality & trends</p>
        <p><strong>• Hybrid Models:</strong> Ensemble methods for 92.3% accuracy</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #00ff88;">📊 Market Intelligence</h3>
        <p>• Real-time price feeds from 25+ exchanges</p>
        <p>• Social sentiment analysis from Twitter/Reddit</p>
        <p>• On-chain analytics & whale tracking</p>
        <p>• Regulatory news impact analysis</p>
    </div>
    """, unsafe_allow_html=True)

with features_grid[1]:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #ff6b6b;">📈 Advanced Analytics</h3>
        <p>• Portfolio risk assessment & optimization</p>
        <p>• Volatility forecasting & stress testing</p>
        <p>• Correlation matrices across 200+ assets</p>
        <p>• Backtesting engine with historical data</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #ffd166;">🔒 Security & Compliance</h3>
        <p>• Bank-grade AES-256 encryption</p>
        <p>• Multi-signature wallet support</p>
        <p>• GDPR & CCPA compliant data handling</p>
        <p>• Regular third-party security audits</p>
    </div>
    """, unsafe_allow_html=True)

with features_grid[2]:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #9d4edd;">⚡ Performance & Scale</h3>
        <p>• Processes 50,000+ transactions/sec</p>
        <p>• <50ms API response time guarantee</p>
        <p>• 99.99% uptime SLA</p>
        <p>• Auto-scaling cloud infrastructure</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #ff9e00;">🌐 Multi-Platform Access</h3>
        <p>• Web dashboard with real-time updates</p>
        <p>• Mobile app for iOS & Android</p>
        <p>• API access for institutional clients</p>
        <p>• Telegram & Discord trading bots</p>
    </div>
    """, unsafe_allow_html=True)

# ====================
# MARKET VISUALIZATION
# ====================
st.markdown('<h2 class="section-header">📈 Live Market Overview</h2>', unsafe_allow_html=True)

# Generate sample cryptocurrency data
np.random.seed(42)
dates = pd.date_range(start='2025-10-01', end='2025-11-28', freq='D')

# Create realistic price movements
btc_price = 85000
eth_price = 4500
sol_price = 180

btc_prices = []
eth_prices = []
sol_prices = []

for i in range(len(dates)):
    # Add some trend + random movement
    btc_trend = 0.0008 if i < 30 else -0.0005
    eth_trend = 0.001 if i < 30 else -0.0003
    sol_trend = 0.0015 if i < 30 else -0.0008
    
    btc_price *= (1 + btc_trend + np.random.normal(0, 0.02))
    eth_price *= (1 + eth_trend + np.random.normal(0, 0.025))
    sol_price *= (1 + sol_trend + np.random.normal(0, 0.03))
    
    btc_prices.append(btc_price)
    eth_prices.append(eth_price)
    sol_prices.append(sol_price)

df = pd.DataFrame({
    'Date': dates,
    'Bitcoin (BTC)': btc_prices,
    'Ethereum (ETH)': eth_prices,
    'Solana (SOL)': sol_prices
})

# Tabs for different visualizations
viz_tab1, viz_tab2, viz_tab3 = st.tabs(["📊 Price Charts", "📉 Market Trends", "📊 Distribution"])

with viz_tab1:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    
    # Create interactive chart
    fig = go.Figure()
    
    colors = ['#F7931A', '#627EEA', '#00FFA3']
    cryptos = ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Solana (SOL)']
    
    for idx, crypto in enumerate(cryptos):
        fig.add_trace(go.Scatter(
            x=df['Date'], y=df[crypto],
            mode='lines',
            name=crypto,
            line=dict(color=colors[idx], width=3),
            fill='tozeroy' if idx == 0 else None,
            fillcolor=f'rgba{tuple(int(colors[idx][i:i+2], 16) for i in (1, 3, 5)) + (0.1,)}' if idx == 0 else None
        ))
    
    fig.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400,
        hovermode='x unified',
        title='Cryptocurrency Price Trends (Oct-Nov 2025)',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with viz_tab2:
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    
    # Calculate daily returns
    returns_df = df.copy()
    for crypto in cryptos:
        returns_df[f'{crypto}_Returns'] = returns_df[crypto].pct_change() * 100
    
    # Create returns heatmap
    fig = go.Figure(data=go.Heatmap(
        z=returns_df[[f'{crypto}_Returns' for crypto in cryptos]].tail(30).T,
        x=returns_df['Date'].tail(30),
        y=cryptos,
        colorscale='RdBu',
        zmid=0,
        colorbar=dict(title='Daily Return %')
    ))
    
    fig.update_layout(
        template='plotly_dark',
        height=400,
        title='Daily Returns Heatmap (Last 30 Days)',
        xaxis_title='Date',
        yaxis_title='Cryptocurrency'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with viz_tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        
        # Market cap distribution
        market_caps = {
            'Cryptocurrency': ['Bitcoin', 'Ethereum', 'Solana', 'Cardano', 'Polkadot', 'Others'],
            'Market Cap ($B)': [850, 380, 45, 18, 12, 95],
            'Color': ['#F7931A', '#627EEA', '#00FFA3', '#0033AD', '#E6007A', '#888888']
        }
        
        fig = px.pie(market_caps, values='Market Cap ($B)', names='Cryptocurrency',
                     color='Cryptocurrency', color_discrete_map=dict(zip(market_caps['Cryptocurrency'], market_caps['Color'])),
                     hole=0.4)
        
        fig.update_layout(
            template='plotly_dark',
            height=350,
            title='Market Capitalization Distribution',
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-box">', unsafe_allow_html=True)
        
        # Volume chart
        volumes = {
            'Cryptocurrency': ['Bitcoin', 'Ethereum', 'Solana', 'Cardano', 'Polkadot'],
            '24h Volume ($B)': [28.5, 12.3, 3.8, 1.2, 0.8],
            'Change (%)': [2.5, 3.2, 8.7, -1.2, 0.5]
        }
        
        vol_df = pd.DataFrame(volumes)
        
        fig = go.Figure(data=[
            go.Bar(name='24h Volume', x=vol_df['Cryptocurrency'], y=vol_df['24h Volume ($B)'],
                  marker_color=['#F7931A', '#627EEA', '#00FFA3', '#0033AD', '#E6007A'])
        ])
        
        fig.update_layout(
            template='plotly_dark',
            height=350,
            title='24h Trading Volume',
            xaxis_title='Cryptocurrency',
            yaxis_title='Volume ($ Billions)',
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ====================
# PERFORMANCE METRICS
# ====================
st.markdown('<h2 class="section-header">📊 Platform Performance Metrics</h2>', unsafe_allow_html=True)

metric_cols = st.columns(4)

with metric_cols[0]:
    st.markdown("""
    <div class="metric-box">
        <h3 style="color: #00d4ff; margin: 0;">🎯 Accuracy</h3>
        <p style="font-size: 2rem; font-weight: bold; margin: 0.5rem 0;">92.3%</p>
        <p style="margin: 0; color: #a0a0c0;">Prediction Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[1]:
    st.markdown("""
    <div class="metric-box">
        <h3 style="color: #00ff88; margin: 0;">⚡ Speed</h3>
        <p style="font-size: 2rem; font-weight: bold; margin: 0.5rem 0;">47ms</p>
        <p style="margin: 0; color: #a0a0c0;">Avg. Response Time</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[2]:
    st.markdown("""
    <div class="metric-box">
        <h3 style="color: #ff6b6b; margin: 0;">📈 Coverage</h3>
        <p style="font-size: 2rem; font-weight: bold; margin: 0.5rem 0;">25+</p>
        <p style="margin: 0; color: #a0a0c0;">Cryptocurrencies</p>
    </div>
    """, unsafe_allow_html=True)

with metric_cols[3]:
    st.markdown("""
    <div class="metric-box">
        <h3 style="color: #ffd166; margin: 0;">💾 Data</h3>
        <p style="font-size: 2rem; font-weight: bold; margin: 0.5rem 0;">1.2M</p>
        <p style="margin: 0; color: #a0a0c0;">Daily Data Points</p>
    </div>
    """, unsafe_allow_html=True)

# ====================
# NAVIGATION GUIDE
# ====================
st.markdown('<h2 class="section-header">🧭 Getting Started Guide</h2>', unsafe_allow_html=True)

guide_col1, guide_col2 = st.columns(2)

with guide_col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📱 Step 1: Dashboard Access</h3>
        <p><strong>1.</strong> Click "Trading Dashboard" button above</p>
        <p><strong>2.</strong> Select cryptocurrency from dropdown menu</p>
        <p><strong>3.</strong> Choose date range for analysis</p>
        <p><strong>4.</strong> Select forecasting model (ARIMA/LSTM/Prophet)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 Step 3: AI Analysis</h3>
        <p><strong>1.</strong> View real-time price predictions</p>
        <p><strong>2.</strong> Analyze confidence intervals</p>
        <p><strong>3.</strong> Compare different model outputs</p>
        <p><strong>4.</strong> Download reports & insights</p>
    </div>
    """, unsafe_allow_html=True)

with guide_col2:
    st.markdown("""
    <div class="feature-card">
        <h3>⚙️ Step 2: Configuration</h3>
        <p><strong>1.</strong> Set forecast horizon (1-90 days)</p>
        <p><strong>2.</strong> Adjust model parameters if needed</p>
        <p><strong>3.</strong> Add custom indicators (RSI, MACD, etc.)</p>
        <p><strong>4.</strong> Configure alerts & notifications</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📚 Step 4: Advanced Features</h3>
        <p><strong>1.</strong> Explore platform documentation</p>
        <p><strong>2.</strong> Meet our expert team members</p>
        <p><strong>3.</strong> Access API for automation</p>
        <p><strong>4.</strong> Join our trading community</p>
    </div>
    """, unsafe_allow_html=True)

# ====================
# FOOTER & CTA
# ====================
st.markdown("---")

footer_col1, footer_col2 = st.columns([2, 1])

with footer_col1:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2 style="color: #00d4ff;">Ready to Revolutionize Your Crypto Trading?</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">Join 10,000+ traders using AI-powered insights for smarter decisions</p>
        
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 2rem;">
            <button class="nav-btn" onclick="window.location.href='pages/1_🏠_Dashboard.py'">
                🚀 Start Trading Analysis
            </button>
            <button class="nav-btn" style="background: linear-gradient(135deg, #00ff88, #00b8ff);" 
                    onclick="window.location.href='pages/2_📋_Description.py'">
                📖 Learn More
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

with footer_col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; border-left: 2px solid #2a2a5a;">
        <h4>🔒 Secure Platform</h4>
        <p style="font-size: 0.9rem; color: #a0a0c0;">Bank-level security • 24/7 monitoring • Regular audits</p>
        
        <h4 style="margin-top: 1.5rem;">📞 Support</h4>
        <p style="font-size: 0.9rem; color: #a0a0c0;">support@cryptoforecast.ai<br>+1 (555) 123-4567</p>
    </div>
    """, unsafe_allow_html=True)

# Final footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #a0a0c0; font-size: 0.9rem; padding: 1rem;">
    <p>© 2025 CryptoForecast AI | Advanced Cryptocurrency Analytics Platform | All Rights Reserved</p>
    <p style="font-size: 0.8rem; opacity: 0.7;">Disclaimer: This platform provides analytical tools, not financial advice. Cryptocurrency investments carry risk.</p>
</div>
""", unsafe_allow_html=True)