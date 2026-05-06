import streamlit as st
import pandas as pd

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="2026 E-com Performance Stack | By Instapulse",
    page_icon="📈",
    layout="wide"
)

# 2. CUSTOM CSS FOR STYLING
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. HERO SECTION
col_hero1, col_hero2 = st.columns([2, 1])

with col_hero1:
    st.title("🚀 The 2026 Media Buying Tech Stack")
    st.subheader("Automate Creative Fatigue & Scale ROAS with AI")
    st.write("""
    Stop wasting thousands on manual video editing and complex funnel builds. 
    As a **Senior Media Buyer** and **MSc in Physics**, I don't believe in "hacks"—I believe in 
    **Performance Efficiency** and **Algorithmic Scaling**.
    """)
    st.info("💡 **Pro Tip:** In 2026, the 'Hook' is 90% of your ad success. These tools automate that 90%.")

with col_hero2:
    st.image("https://via.placeholder.com/300x300?text=Instapulse+Agency", caption="Managed by Instapulse Agency")

st.divider()

# 4. PERFORMANCE ROI CALCULATOR (Physics/Math Inspired)
st.header("📊 Performance Efficiency Calculator")
st.write("Calculate how much you save by switching from manual editing to AI-automated creatives.")

c1, c2, c3 = st.columns(3)
with c1:
    current_cost = st.number_input("Monthly Editor Salary ($)", value=2500, step=100)
with c2:
    vids_per_month = st.number_input("Videos Needed per Month", value=20, step=1)
with c3:
    ai_cost = st.number_input("AI Tool Monthly Cost ($)", value=30, step=5)

# LaTeX for the Efficiency Formula
st.latex(r"Savings = (Cost_{Manual} - Cost_{AI}) + (\Delta Time \times Hourly Rate)")

monthly_savings = current_cost - ai_cost
st.success(f"### Estimated Monthly Savings: **${monthly_savings:,}**")

st.divider()

# 5. THE HERO STACK (Affiliate Links)
st.header("🛠️ The Core Infrastructure")

# Tool 1: InVideo AI
t1_col1, t1_col2 = st.columns([1, 2])
with t1_col1:
    st.image("https://via.placeholder.com/400x250?text=InVideo+AI+Demo")
with t1_col2:
    st.subheader("1. InVideo AI: The 'Ad Creator' Engine")
    st.write("""
    * **Best For:** Rapidly testing 10+ variations of a single ad concept.
    * **Why it works:** It uses an 'Idea-to-Video' LLM that understands high-converting hooks.
    * **My Result:** Reduced creative production time from 4 days to 4 minutes.
    """)
    st.link_button("👉 Claim 50 Free AI Minutes", "https://your-invideo-affiliate-link.com")

st.write("---")

# Tool 2: Systeme.io
t2_col1, t2_col2 = st.columns([1, 2])
with t2_col1:
    st.image("https://via.placeholder.com/400x250?text=Systeme.io+Funnel")
with t2_col2:
    st.subheader("2. Systeme.io: The Conversion Backend")
    st.write("""
    * **Best For:** Hosting your landing pages, emails, and affiliate loops in one place.
    * **Why it works:** Zero-lag page loading speeds (Critical for Meta Ads ROAS).
    * **My Result:** 100% replacement for ClickFunnels and Mailchimp at 1/10th the cost.
    """)
    st.link_button("👉 Launch Your Free Funnel Now", "https://your-systeme-affiliate-link.com")

st.divider()

# 6. FAQ & TRUST SECTION
with st.expander("❓ FAQ: Why trust this stack?"):
    st.write("""
    **Is this only for beginners?**  
    No. I use these tools to manage media buying for brands achieving peak turnovers of **8 Crore ($1M USD)**. Efficiency is the only way to scale.
    
    **Do I need to know coding?**  
    No. These are no-code tools. I've built this dashboard using Python so you don't have to touch a single line of JavaScript.
    """)

# 7. FOOTER / LEAD CAPTURE
st.write("### 📬 Get the 2026 Scaling SOP")
email = st.text_input("Enter your email for my private Media Buying SOPs:")
if st.button("Send me the SOP"):
    st.write(f"Thanks! I'll reach out to **{email}** shortly.")

st.caption("© 2026 Instapulse Agency | Jaipur, India. Managed by a Senior Media Buyer.")