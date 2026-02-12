import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Platform Description - CryptoForecast AI",
    page_icon="📋",
    layout="wide"
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
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 212, 255, 0.4);
        border-color: #00d4ff;
    }
    
    /* Section headers */
    .section-header {
        border-left: 5px solid #00ff88;
        padding-left: 15px;
        margin: 2rem 0 1rem 0;
        color: #ffffff;
    }
    
    /* Feature icon styling */
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    /* Metric boxes */
    .metric-box {
        background: rgba(0, 212, 255, 0.1);
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 5px solid #00d4ff;
        margin: 0.5rem 0;
        text-align: center;
    }
    
    /* Tech stack badges */
    .tech-badge {
        display: inline-block;
        background: rgba(0, 212, 255, 0.2);
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        font-size: 0.9rem;
        border: 1px solid rgba(0, 212, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ====================
# MAIN HEADER
# ====================
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3rem; margin: 0; font-weight: 800;">📋 CRYPTOFORECAST AI PLATFORM</h1>
    <p style="font-size: 1.5rem; margin: 1rem 0 0 0; opacity: 0.9;">Complete Platform Description & Features</p>
</div>
""", unsafe_allow_html=True)

# Back to home button
if st.button("🏠 Back to Home", type="secondary"):
    st.switch_page("streamlit_app.py")

# ====================
# PLATFORM OVERVIEW
# ====================
st.markdown("""
<div style="background: rgba(30, 30, 60, 0.7); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
    <h2 style="color: #00d4ff; margin-top: 0;">🔍 Platform Overview</h2>
    <p style="font-size: 1.1rem; line-height: 1.6;">
        CryptoForecast AI is an enterprise-grade cryptocurrency analytics platform that leverages 
        cutting-edge machine learning algorithms to provide accurate price predictions, 
        comprehensive market analysis, and actionable trading insights. Our platform is designed 
        for both retail traders and institutional investors seeking data-driven decision-making tools.
    </p>
    <p style="font-size: 1.1rem; line-height: 1.6;">
        With real-time data processing, multiple forecasting models, and advanced visualization tools, 
        we empower users to navigate the volatile cryptocurrency markets with confidence and precision.
    </p>
</div>
""", unsafe_allow_html=True)

# ====================
# KEY FEATURES SECTION
# ====================
st.markdown('<h2 class="section-header">✨ Key Features & Capabilities</h2>', unsafe_allow_html=True)

# Create 3 columns for features
feature_cols = st.columns(3)

with feature_cols[0]:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🤖</span>
        <h3 style="color: #00d4ff;">Multiple ML Models</h3>
        <p><strong>ARIMA:</strong> Traditional time series forecasting with statistical accuracy</p>
        <p><strong>LSTM Neural Networks:</strong> Deep learning for complex pattern recognition</p>
        <p><strong>Prophet:</strong> Facebook's model for seasonality and trend analysis</p>
        <p><strong>Hybrid Models:</strong> Ensemble approaches combining multiple algorithms</p>
        <p style="margin-top: 1rem; color: #a0a0c0; font-size: 0.9rem;">
            <strong>Result:</strong> 92.3% prediction accuracy across all models
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">⚡</span>
        <h3 style="color: #ff6b6b;">High Performance</h3>
        <p>• Optimized algorithms processing 50,000+ data points per second</p>
        <p>• Parallel model training reducing computation time by 70%</p>
        <p>• Real-time inference with <50ms latency</p>
        <p>• Distributed computing across GPU clusters</p>
        <p>• Efficient memory management for large datasets</p>
    </div>
    """, unsafe_allow_html=True)

with feature_cols[1]:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📈</span>
        <h3 style="color: #00ff88;">Real-time Analysis</h3>
        <p>• Live price feeds from 25+ cryptocurrency exchanges</p>
        <p>• Minute-level precision with websocket connections</p>
        <p>• Social media sentiment analysis (Twitter, Reddit, Telegram)</p>
        <p>• On-chain analytics with whale tracking</p>
        <p>• News aggregation and impact scoring</p>
        <p>• Order book depth analysis in real-time</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📊</span>
        <h3 style="color: #ffd166;">Comprehensive Dashboards</h3>
        <p>• Interactive charts with zoom and export capabilities</p>
        <p>• Customizable widgets for personalized layouts</p>
        <p>• Multiple chart types (candlestick, line, bar, heatmap)</p>
        <p>• Real-time alerts and notifications</p>
        <p>• Portfolio performance tracking</p>
        <p>• Mobile-responsive design</p>
    </div>
    """, unsafe_allow_html=True)

with feature_cols[2]:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🔒</span>
        <h3 style="color: #9d4edd;">Secure & Reliable</h3>
        <p>• Bank-grade AES-256 encryption for all data</p>
        <p>• Multi-factor authentication and SSO support</p>
        <p>• 99.99% uptime guarantee with auto-failover</p>
        <p>• Regular security audits by third-party firms</p>
        <p>• GDPR and CCPA compliant data handling</p>
        <p>• Encrypted database and secure API endpoints</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🔄</span>
        <h3 style="color: #ff9e00;">Automated Updates</h3>
        <p>• Continuous model retraining with new data</p>
        <p>• Automatic feature engineering pipelines</p>
        <p>• Scheduled database maintenance and optimization</p>
        <p>• Real-time model performance monitoring</p>
        <p>• Auto-scaling infrastructure based on demand</p>
        <p>• Daily backup and recovery systems</p>
    </div>
    """, unsafe_allow_html=True)

# ====================
# ADDITIONAL FEATURES
# ====================
st.markdown('<h2 class="section-header">🚀 Advanced Features</h2>', unsafe_allow_html=True)

# Create two columns for additional features
adv_cols = st.columns(2)

with adv_cols[0]:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #00d4ff;">📊 Advanced Analytics</h3>
        <p><strong>• Portfolio Optimization:</strong> Risk-adjusted return maximization</p>
        <p><strong>• Correlation Analysis:</strong> Multi-asset relationship mapping</p>
        <p><strong>• Volatility Forecasting:</strong> GARCH and stochastic models</p>
        <p><strong>• Backtesting Engine:</strong> Historical strategy validation</p>
        <p><strong>• Sentiment Analysis:</strong> NLP-powered market mood</p>
        <p><strong>• Anomaly Detection:</strong> AI-powered outlier identification</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #00ff88;">🌐 Multi-Platform Access</h3>
        <p><strong>• Web Dashboard:</strong> Full-featured browser interface</p>
        <p><strong>• Mobile Apps:</strong> iOS and Android native applications</p>
        <p><strong>• API Access:</strong> RESTful API for institutional clients</p>
        <p><strong>• Trading Bots:</strong> Integration with popular trading platforms</p>
        <p><strong>• Webhook Support:</strong> Custom alert delivery</p>
        <p><strong>• Data Feeds:</strong> Real-time streaming for developers</p>
    </div>
    """, unsafe_allow_html=True)

with adv_cols[1]:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #ff6b6b;">🤝 Collaboration Tools</h3>
        <p><strong>• Team Workspaces:</strong> Shared analysis environments</p>
        <p><strong>• Report Sharing:</strong> PDF and Excel export options</p>
        <p><strong>• Comment System:</strong> Collaborative analysis notes</p>
        <p><strong>• Version Control:</strong> Model and analysis history</p>
        <p><strong>• Audit Logs:</strong> Complete activity tracking</p>
        <p><strong>• Role-Based Access:</strong> Custom permission levels</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 style="color: #ff9e00;">📚 Educational Resources</h3>
        <p><strong>• Interactive Tutorials:</strong> Step-by-step platform guides</p>
        <p><strong>• Market Insights:</strong> Daily analysis and reports</p>
        <p><strong>• Model Documentation:</strong> Technical specifications</p>
        <p><strong>• Video Library:</strong> Tutorial videos and webinars</p>
        <p><strong>• Community Forum:</strong> User discussions and support</p>
        <p><strong>• Research Papers:</strong> Academic methodology</p>
    </div>
    """, unsafe_allow_html=True)

# ====================
# TECHNOLOGY STACK
# ====================
st.markdown('<h2 class="section-header">💻 Technology Stack</h2>', unsafe_allow_html=True)

tech_cols = st.columns(4)

tech_stack = [
    ("Python 3.10", "Backend & Machine Learning", "#3776AB"),
    ("TensorFlow 2.13", "Deep Learning Framework", "#FF6F00"),
    ("Streamlit", "Frontend & Dashboard", "#FF4B4B"),
    ("PostgreSQL", "Database Management", "#336791"),
    ("Docker", "Containerization", "#2496ED"),
    ("AWS EC2", "Cloud Infrastructure", "#FF9900"),
    ("Redis", "Caching Layer", "#DC382D"),
    ("FastAPI", "API Framework", "#009688"),
    ("Plotly", "Data Visualization", "#3F4F75"),
    ("Scikit-learn", "ML Algorithms", "#F7931E"),
    ("Pandas", "Data Processing", "#150458"),
    ("GitHub Actions", "CI/CD Pipeline", "#2088FF")
]

for idx, (tech, desc, color) in enumerate(tech_stack):
    with tech_cols[idx % 4]:
        st.markdown(f"""
        <div style="background: rgba{tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (0.2,)}; 
                    padding: 1rem; border-radius: 10px; border-left: 4px solid {color}; margin-bottom: 1rem;">
            <h4 style="margin: 0; color: {color};">{tech}</h4>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #a0a0c0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ====================
# PERFORMANCE METRICS
# ====================
st.markdown('<h2 class="section-header">📊 Platform Performance Metrics</h2>', unsafe_allow_html=True)

metric_cols = st.columns(5)

metrics = [
    ("Prediction Accuracy", "92.3%", "+2.1%", "#00d4ff"),
    ("Response Time", "<50ms", "avg", "#00ff88"),
    ("Uptime", "99.99%", "SLA", "#ff6b6b"),
    ("Data Points", "1.2M/day", "processed", "#ffd166"),
    ("Supported Cryptos", "25+", "assets", "#9d4edd")
]

for idx, (label, value, delta, color) in enumerate(metrics):
    with metric_cols[idx]:
        st.markdown(f"""
        <div class="metric-box">
            <h4 style="color: {color}; margin: 0;">{label}</h4>
            <p style="font-size: 2rem; font-weight: bold; margin: 0.5rem 0;">{value}</p>
            <p style="margin: 0; color: #a0a0c0;">{delta}</p>
        </div>
        """, unsafe_allow_html=True)

# ====================
# HOW IT WORKS
# ====================
st.markdown('<h2 class="section-header">🛠️ How It Works</h2>', unsafe_allow_html=True)

steps = [
    ("1", "Data Collection", "Aggregate data from 25+ exchanges, news APIs, social media, and on-chain sources"),
    ("2", "Data Processing", "Clean, normalize, and engineer features using automated pipelines"),
    ("3", "Model Training", "Train multiple ML models with cross-validation and hyperparameter tuning"),
    ("4", "Model Evaluation", "Validate predictions against historical data and select best-performing model"),
    ("5", "Deployment", "Deploy model to production with real-time inference capabilities"),
    ("6", "Monitoring", "Continuously monitor model performance and retrain as needed")
]

for step_num, title, description in steps:
    with st.expander(f"Step {step_num}: {title}", expanded=False):
        st.markdown(f"""
        <div style="padding: 1rem; background: rgba(30, 30, 60, 0.5); border-radius: 10px;">
            <p style="margin: 0; line-height: 1.6;">{description}</p>
        </div>
        """, unsafe_allow_html=True)

# ====================
# CALL TO ACTION
# ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 136, 255, 0.1)); 
            border-radius: 15px; margin: 2rem 0;">
    <h2 style="color: #00d4ff;">Ready to Experience Advanced Crypto Analytics?</h2>
    <p style="font-size: 1.2rem; margin: 1rem 0;">Start using our platform today with a free 14-day trial</p>
    
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 2rem;">
        <button onclick="window.location.href='pages/1_🏠_Dashboard.py'" 
                style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                       color: white; padding: 15px 30px; border: none; border-radius: 12px; 
                       font-size: 16px; font-weight: bold; cursor: pointer;">
            🚀 Start Free Trial
        </button>
        
        <button onclick="window.location.href='streamlit_app.py'" 
                style="background: transparent; color: #00d4ff; padding: 15px 30px; 
                       border: 2px solid #00d4ff; border-radius: 12px; 
                       font-size: 16px; font-weight: bold; cursor: pointer;">
            ← Back to Home
        </button>
    </div>
</div>
""", unsafe_allow_html=True)

# ====================
# FOOTER
# ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #a0a0c0; font-size: 0.9rem; padding: 1rem;">
    <p>© 2025 CryptoForecast AI | Platform Description v2.0 | Last Updated: December 2025</p>
    <p style="font-size: 0.8rem; opacity: 0.7;">
        All features are subject to availability. Platform performance may vary based on market conditions.
    </p>
</div>
""", unsafe_allow_html=True)