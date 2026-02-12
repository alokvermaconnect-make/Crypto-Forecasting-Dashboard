import streamlit as st

st.set_page_config(
    page_title="Team Overview - CryptoForecast",
    layout="wide"
)

st.title("👥 Team Overview")

st.markdown("""
<div style="background: linear-gradient(135deg, #6a11cb, #2575fc); 
            padding: 2rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
    <h2 style="color: white; margin-bottom: 0;">Meet Our Team</h2>
    <p style="font-size: 1.1rem; opacity: 0.9;">Dedicated data analyst aspirantents</p>
</div>
""", unsafe_allow_html=True)

# Core Team Members
st.header("🌟 Team Members")

team_members = [
    {
        "name": "RAKSHA KS",
        "studies": "BE Final Year",
        "avatar": "👩‍🔬",
        "email": "rakshashivakumar4@gmail.com"
    },
    {
        "name": "Alok Verma",
        "studies": "BCA",
        "avatar": "👨‍💻",
        "email": "vermaalok484@gmail.com"
    },
    {
        "name": "Pawar Akshitha",
        "studies": "BTech",
        "avatar": "👩‍💼",
        "email": "pawararakshitha25@gmail.com"
    },
    {
        "name": "Shashanka SM",
        "studies": "BTech",
        "avatar": "👨‍🎓",
        "email": "shashanka.sm@example.com"
    },
    {
        "name": "Krishna Vekariya",
        "studies": "BE",
        "avatar": "👨‍💼",
        "email": "vekariya.krishna768@gmail.com"
    },
    {
        "name": "Chandupatla Samyana Reddy",
        "studies": "BTech",
        "avatar": "👨‍🏫",
        "email": "2210040032ece@gmail.com"
    }
]

# Display team members in a grid
cols_per_row = 3
for i in range(0, len(team_members), cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(team_members):
            member = team_members[i + j]
            with cols[j]:
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                            border: 1px solid #e1e4e8; margin-bottom: 1.5rem;
                            box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    <div style="font-size: 3rem; text-align: center; margin-bottom: 0.5rem;">{member['avatar']}</div>
                    <h3 style="text-align: center; color: #333; margin-bottom: 0.5rem;">{member['name']}</h3>
                    <p style="text-align: center; color: #666; margin-bottom: 1rem; font-size: 0.9rem;">
                        {member['studies']}
                    </p>
                    <div style="text-align: center; padding-top: 0.5rem; border-top: 1px solid #eee;">
                        <small style="color: #6a11cb;">📧 {member['email']}</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# Simple stats
st.header("📊 Quick Stats")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Team Size", "6", "")
with col2:
    st.metric("Students", "6", "")
with col3:
    st.metric("Domains", "2", "Tech + Finance")

# Footer
st.markdown("---")
st.caption("© 2025 CryptoForecast AI")