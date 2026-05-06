import streamlit as st
import pandas as pd

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="2026 D2C Performance Stack | By InstaPulse",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0D0F14;
    color: #E8EAF0;
}
.main { background-color: #0D0F14 !important; }
section[data-testid="stSidebar"] { display: none; }
.block-container { padding: 2rem 3rem 4rem 3rem !important; max-width: 1200px; }

/* ── Typography ── */
h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; letter-spacing: -0.02em; }

/* ── Divider ── */
hr { border: none; border-top: 1px solid #1E2230 !important; margin: 2.5rem 0 !important; }

/* ── Hero Badge ── */
.badge {
    display: inline-block;
    background: linear-gradient(135deg, #FF4D6D22, #FF4D6D44);
    border: 1px solid #FF4D6D66;
    color: #FF8FA3;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 20px;
    margin-bottom: 1rem;
}

/* ── Section Labels ── */
.section-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #FF4D6D;
    margin-bottom: 0.4rem;
}

/* ── KPI Cards ── */
.kpi-card {
    background: #13161F;
    border: 1px solid #1E2230;
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    transition: border-color 0.2s ease;
}
.kpi-card:hover { border-color: #FF4D6D55; }
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.kpi-value span { color: #FF4D6D; }
.kpi-label { font-size: 0.8rem; color: #6B7394; font-weight: 500; }

/* ── Tool Cards ── */
.tool-card {
    background: #13161F;
    border: 1px solid #1E2230;
    border-radius: 14px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}
.tool-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, #FF4D6D, #FF8C42);
    border-radius: 4px 0 0 4px;
}
.tool-tag {
    display: inline-block;
    background: #1E2230;
    color: #A0A8C0;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 4px;
    margin-right: 6px;
    margin-bottom: 6px;
}
.tool-tag.hot { background: #FF4D6D22; color: #FF8FA3; border: 1px solid #FF4D6D44; }
.commission-badge {
    background: #0D2A1A;
    border: 1px solid #1A5C36;
    color: #4ADE80;
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    padding: 8px 16px;
    border-radius: 8px;
    display: inline-block;
    margin: 0.8rem 0;
}

/* ── Metric Row ── */
.metric-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin: 0.8rem 0;
}
.metric-chip {
    background: #1A1E2C;
    border: 1px solid #252B3D;
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 0.78rem;
    color: #A0A8C0;
}
.metric-chip strong { color: #E8EAF0; }

/* ── Buttons ── */
.stLinkButton a, .stButton > button {
    background: linear-gradient(135deg, #FF4D6D, #FF2D55) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.7rem 1.5rem !important;
    transition: opacity 0.2s ease !important;
    text-decoration: none !important;
}
.stLinkButton a:hover, .stButton > button:hover { opacity: 0.85 !important; }

/* ── Calculator ── */
.calc-box {
    background: #13161F;
    border: 1px solid #1E2230;
    border-radius: 14px;
    padding: 2rem;
}
.result-highlight {
    background: linear-gradient(135deg, #0D2A1A, #0A2010);
    border: 1px solid #1A5C36;
    border-radius: 10px;
    padding: 1.2rem 1.6rem;
    margin-top: 1rem;
}
.result-highlight .big-num {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #4ADE80;
    line-height: 1;
}
.result-sub { font-size: 0.82rem; color: #6B7394; margin-top: 0.3rem; }

/* ── Number inputs ── */
.stNumberInput label { color: #A0A8C0 !important; font-size: 0.82rem !important; }
.stNumberInput input {
    background: #1A1E2C !important;
    border: 1px solid #252B3D !important;
    color: #E8EAF0 !important;
    border-radius: 8px !important;
}

/* ── Text input ── */
.stTextInput label { color: #A0A8C0 !important; }
.stTextInput input {
    background: #1A1E2C !important;
    border: 1px solid #252B3D !important;
    color: #E8EAF0 !important;
    border-radius: 8px !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: #13161F !important;
    border: 1px solid #1E2230 !important;
    border-radius: 10px !important;
    color: #E8EAF0 !important;
    font-weight: 600 !important;
}
.streamlit-expanderContent {
    background: #0F1219 !important;
    border: 1px solid #1E2230 !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
}

/* ── Info/Success boxes ── */
.stAlert { border-radius: 10px !important; border: none !important; }

/* ── Table ── */
.stDataFrame { border-radius: 10px !important; overflow: hidden; }

/* ── Selectbox ── */
.stSelectbox label { color: #A0A8C0 !important; font-size: 0.82rem !important; }
div[data-baseweb="select"] > div {
    background: #1A1E2C !important;
    border: 1px solid #252B3D !important;
    border-radius: 8px !important;
    color: #E8EAF0 !important;
}

/* ── Footer ── */
.footer {
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid #1E2230;
    text-align: center;
    color: #3D4460;
    font-size: 0.78rem;
    letter-spacing: 0.04em;
}
</style>
""", unsafe_allow_html=True)

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="badge">⚡ Live Stack · Jaipur, India · 2026</div>', unsafe_allow_html=True)

col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("""
    <h1 style="font-size: 3.2rem; font-weight: 800; margin: 0 0 0.5rem 0; line-height: 1.1;">
        The D2C Performance Stack<br>
        <span style="color: #FF4D6D;">I Actually Use</span> in My Agency
    </h1>
    <p style="font-size: 1.05rem; color: #8890AA; max-width: 620px; line-height: 1.7; margin-bottom: 1.5rem;">
        I run <strong style="color:#E8EAF0;">InstaPulse</strong> — a boutique performance marketing agency managing 
        Meta Ads + Shopify for D2C brands across ethnic wear, gemstones, and fashion. 
        These are the exact tools powering ₹50L+ in managed ad spend. No filler, no fluff.
    </p>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value">₹<span>50L+</span></div>
            <div class="kpi-label">Managed Ad Spend</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value"><span>5</span></div>
            <div class="kpi-label">Active D2C Clients</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-value"><span>3</span></div>
            <div class="kpi-label">7-Figure Brands Built</div>
        </div>""", unsafe_allow_html=True)

with col_h2:
    st.markdown("""
    <div style="background: #13161F; border: 1px solid #1E2230; border-radius: 14px; padding: 1.6rem; margin-top: 1rem;">
        <div class="section-label">Stack Highlights</div>
        <div style="margin-top: 0.8rem; display: flex; flex-direction: column; gap: 0.6rem;">
            <div style="display: flex; align-items: center; gap: 0.6rem; font-size: 0.85rem; color: #A0A8C0;">
                <span style="color: #4ADE80;">✓</span> Meta Ads + CAPI
            </div>
            <div style="display: flex; align-items: center; gap: 0.6rem; font-size: 0.85rem; color: #A0A8C0;">
                <span style="color: #4ADE80;">✓</span> Shopify + GA4
            </div>
            <div style="display: flex; align-items: center; gap: 0.6rem; font-size: 0.85rem; color: #A0A8C0;">
                <span style="color: #4ADE80;">✓</span> Python Automation
            </div>
            <div style="display: flex; align-items: center; gap: 0.6rem; font-size: 0.85rem; color: #A0A8C0;">
                <span style="color: #4ADE80;">✓</span> AI Creative Tools
            </div>
            <div style="display: flex; align-items: center; gap: 0.6rem; font-size: 0.85rem; color: #A0A8C0;">
                <span style="color: #4ADE80;">✓</span> Telegram Briefings
            </div>
        </div>
        <div style="margin-top: 1.2rem; padding-top: 1rem; border-top: 1px solid #1E2230;">
            <div style="font-size: 0.75rem; color: #3D4460;">MSc Physics · 19 Months Agency</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ─── CALCULATOR ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">ROI Calculator</div>', unsafe_allow_html=True)
st.markdown('<h2 style="margin-top: 0;">Performance Efficiency Calculator</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #8890AA; margin-bottom: 1.5rem;">Reverse-engineer the cost of manual creative production vs. AI automation. Based on real agency benchmarks.</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="calc-box">', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        editor_cost = st.number_input("Monthly Editor Cost ($)", value=500, step=50,
                                       help="Freelancer or in-house editor monthly cost")
    with c2:
        vids_per_month = st.number_input("Ad Creatives Needed / Month", value=20, step=5)
    with c3:
        hours_per_video = st.number_input("Hours per Creative (Manual)", value=3.0, step=0.5)
    with c4:
        ai_tool_cost = st.number_input("AI Tool Monthly Cost ($)", value=30, step=5)

    hourly_rate = editor_cost / (vids_per_month * hours_per_video) if (vids_per_month * hours_per_video) > 0 else 0
    time_saved_hrs = vids_per_month * (hours_per_video - 0.2)
    monthly_savings = editor_cost - ai_tool_cost
    annual_savings = monthly_savings * 12

    st.latex(r"\text{Savings} = (C_{\text{manual}} - C_{\text{AI}}) + (\Delta t \times R_{\text{hourly}})")

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown(f"""
        <div class="result-highlight">
            <div style="font-size: 0.75rem; color: #4ADE80; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.4rem;">Monthly Savings</div>
            <div class="big-num">${monthly_savings:,.0f}</div>
            <div class="result-sub">vs. current manual spend</div>
        </div>""", unsafe_allow_html=True)
    with r2:
        st.markdown(f"""
        <div class="result-highlight">
            <div style="font-size: 0.75rem; color: #4ADE80; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.4rem;">Annual Savings</div>
            <div class="big-num">${annual_savings:,.0f}</div>
            <div class="result-sub">reinvest into ad spend</div>
        </div>""", unsafe_allow_html=True)
    with r3:
        st.markdown(f"""
        <div class="result-highlight">
            <div style="font-size: 0.75rem; color: #4ADE80; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.4rem;">Hours Freed / Month</div>
            <div class="big-num">{time_saved_hrs:.0f}h</div>
            <div class="result-sub">for strategy, not editing</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ─── CORE STACK ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">The Core Stack</div>', unsafe_allow_html=True)
st.markdown('<h2 style="margin-top: 0;">Tools I Use. Clients I Recommend. Links I Trust.</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #8890AA; margin-bottom: 2rem;">Every tool below is either used daily in my agency or deployed for clients. Affiliate links marked clearly — I only recommend what I\'d bill to a client account.</p>', unsafe_allow_html=True)

# ── Tool 1: Shopify ──
with st.container():
    st.markdown("""
    <div class="tool-card">
        <span class="tool-tag hot">🔥 Primary Platform</span>
        <span class="tool-tag">E-commerce</span>
        <span class="tool-tag">Affiliate</span>
        <h3 style="margin: 0.8rem 0 0.3rem 0; font-size: 1.4rem;">1. Shopify — The Store Operating System</h3>
        <div class="commission-badge">💰 $150 per referred merchant</div>
        <p style="color: #8890AA; font-size: 0.9rem; line-height: 1.7; margin: 0.5rem 0 1rem 0;">
            I manage 4 active Shopify stores including my own D2C brand Atharva Jaipur (cotton kurtis). 
            Built custom Horizon theme sections, COD-hide app, geo-blocking, and full GA4 + Meta Pixel + CAPI pipelines. 
            If you're launching a D2C brand, there is no better starting point.
        </p>
        <div class="metric-row">
            <div class="metric-chip"><strong>Cookie</strong>: 30 days</div>
            <div class="metric-chip"><strong>Payout</strong>: PayPal / Wire</div>
            <div class="metric-chip"><strong>My Use</strong>: 4 client stores</div>
            <div class="metric-chip"><strong>Min Payout</strong>: $25</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 Start Your Shopify Store (Free Trial)", "https://partners.shopify.com")

st.write("")

# ── Tool 2: Hostinger ──
with st.container():
    st.markdown("""
    <div class="tool-card">
        <span class="tool-tag hot">🔥 High Commission</span>
        <span class="tool-tag">Hosting</span>
        <span class="tool-tag">Affiliate</span>
        <h3 style="margin: 0.8rem 0 0.3rem 0; font-size: 1.4rem;">2. Hostinger — Landing Pages & Backend Hosting</h3>
        <div class="commission-badge">💰 ₹2,000–₹5,000 per sale</div>
        <p style="color: #8890AA; font-size: 0.9rem; line-height: 1.7; margin: 0.5rem 0 1rem 0;">
            I recommend Hostinger to every client who needs a landing page, portfolio site, or product microsite 
            outside their main Shopify store. Reliable uptime, Indian servers for low-latency, and 
            the affiliate program pays some of the highest flat commissions in the hosting category.
        </p>
        <div class="metric-row">
            <div class="metric-chip"><strong>Cookie</strong>: 30 days</div>
            <div class="metric-chip"><strong>Payout</strong>: Wire Transfer</div>
            <div class="metric-chip"><strong>Commission</strong>: ₹2K–₹5K / sale</div>
            <div class="metric-chip"><strong>Approval</strong>: Instant</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 Get Hosting (Up to 80% Off)", "https://hostinger.com/affiliates")

st.write("")

# ── Tool 3: InVideo AI ──
with st.container():
    st.markdown("""
    <div class="tool-card">
        <span class="tool-tag">AI Creative</span>
        <span class="tool-tag">Video Ads</span>
        <span class="tool-tag">Affiliate</span>
        <h3 style="margin: 0.8rem 0 0.3rem 0; font-size: 1.4rem;">3. InVideo AI — Ad Creative at Scale</h3>
        <div class="commission-badge">💰 25–50% recurring commission</div>
        <p style="color: #8890AA; font-size: 0.9rem; line-height: 1.7; margin: 0.5rem 0 1rem 0;">
            For ethnic wear and fashion clients, I need 10–15 ad variants per week without a full editing pipeline. 
            InVideo AI's Idea-to-Video engine handles hooks, B-roll selection, and captions automatically. 
            Best for rapid creative testing on Meta Ads when your budget doesn't support a video team.
        </p>
        <div class="metric-row">
            <div class="metric-chip"><strong>Cookie</strong>: 60 days</div>
            <div class="metric-chip"><strong>Commission</strong>: 25–50% recurring</div>
            <div class="metric-chip"><strong>Payout</strong>: PayPal</div>
            <div class="metric-chip"><strong>Best For</strong>: Fashion/Apparel ads</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 Claim 50 Free AI Minutes", "https://invideo.io/affiliate")

st.write("")

# ── Tool 4: SEMrush ──
with st.container():
    st.markdown("""
    <div class="tool-card">
        <span class="tool-tag hot">💎 High Ticket</span>
        <span class="tool-tag">SEO / Analytics</span>
        <span class="tool-tag">Affiliate</span>
        <h3 style="margin: 0.8rem 0 0.3rem 0; font-size: 1.4rem;">4. SEMrush — Competitive Intelligence for D2C</h3>
        <div class="commission-badge">💰 $200 per sale · 120-day cookie</div>
        <p style="color: #8890AA; font-size: 0.9rem; line-height: 1.7; margin: 0.5rem 0 1rem 0;">
            I use SEMrush for competitor analysis on every new D2C client onboarding — specifically 
            keyword gaps, backlink profiles, and ad copy teardowns. One sale from this affiliate pays 
            more than a month of Amazon commissions. Highest-ticket program I actively promote.
        </p>
        <div class="metric-row">
            <div class="metric-chip"><strong>Cookie</strong>: 120 days</div>
            <div class="metric-chip"><strong>Commission</strong>: $200 / sale</div>
            <div class="metric-chip"><strong>Payout</strong>: Wire / PayPal</div>
            <div class="metric-chip"><strong>Min Payout</strong>: $50</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 Try SEMrush Free for 14 Days", "https://semrush.com/lp/affiliate")

st.write("")

# ── Tool 5: Canva Pro ──
with st.container():
    st.markdown("""
    <div class="tool-card">
        <span class="tool-tag">Design</span>
        <span class="tool-tag">Social Creative</span>
        <span class="tool-tag">Affiliate</span>
        <h3 style="margin: 0.8rem 0 0.3rem 0; font-size: 1.4rem;">5. Canva Pro — Client Reports & Ad Creatives</h3>
        <div class="commission-badge">💰 $36 per annual subscription</div>
        <p style="color: #8890AA; font-size: 0.9rem; line-height: 1.7; margin: 0.5rem 0 1rem 0;">
            My weekly client reports, ad storyboards, and social media creatives for Doriya Jaipur and 
            GemSpeak all go through Canva Pro. I recommend it to every new client who needs to produce 
            brand content without a designer. Easy conversion because almost everyone already uses Canva Free.
        </p>
        <div class="metric-row">
            <div class="metric-chip"><strong>Cookie</strong>: 30 days</div>
            <div class="metric-chip"><strong>Commission</strong>: $36 / annual</div>
            <div class="metric-chip"><strong>Approval</strong>: Instant</div>
            <div class="metric-chip"><strong>Conversion</strong>: High (warm audience)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("👉 Try Canva Pro Free for 30 Days", "https://canva.com/affiliates")

st.divider()

# ─── COMMISSION COMPARISON TABLE ──────────────────────────────────────────────
st.markdown('<div class="section-label">Revenue Math</div>', unsafe_allow_html=True)
st.markdown('<h2 style="margin-top: 0;">How Many Sales to Hit $20/Day?</h2>', unsafe_allow_html=True)

target = st.slider("Adjust Daily Target ($)", min_value=10, max_value=100, value=20, step=5)

data = {
    "Program": ["Shopify Partners", "SEMrush", "Hostinger (₹)", "Systeme.io", "Canva Pro", "InVideo AI", "Amazon Associates"],
    "Commission": [150, 200, 60, 25, 36, 15, 1.5],
    "Cookie (days)": [30, 120, 30, 180, 30, 60, 1],
    "Type": ["One-time", "One-time", "One-time", "Recurring", "One-time", "Recurring", "Per sale"],
}
df = pd.DataFrame(data)
df["Sales/Day Needed"] = (target / df["Commission"]).round(2)
df["Sales/Month Needed"] = ((target * 30) / df["Commission"]).round(1)
df["Monthly Revenue @ 1 sale/day"] = (df["Commission"] * 30).map(lambda x: f"${x:,.0f}")
df["Effort Level"] = ["🟢 Low", "🟢 Low", "🟢 Low", "🟡 Medium", "🟡 Medium", "🟡 Medium", "🔴 High"]

display_df = df[["Program", "Commission", "Sales/Day Needed", "Sales/Month Needed",
                  "Monthly Revenue @ 1 sale/day", "Cookie (days)", "Effort Level"]].copy()
display_df["Commission"] = display_df["Commission"].map(lambda x: f"${x}")

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
)

st.caption("💡 Shopify: just 4 referrals/month = $600. SEMrush: 3 referrals/month = $600. These two alone can hit the target.")

st.divider()

# ─── AUTOMATION SECTION ───────────────────────────────────────────────────────
st.markdown('<div class="section-label">Agency Automation</div>', unsafe_allow_html=True)
st.markdown('<h2 style="margin-top: 0;">The Python Pipeline Behind InstaPulse</h2>', unsafe_allow_html=True)

a1, a2 = st.columns(2)
with a1:
    st.markdown("""
    <div style="background: #13161F; border: 1px solid #1E2230; border-radius: 14px; padding: 1.6rem;">
        <div style="font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #FF4D6D; margin-bottom: 1rem;">Morning Automation Stack</div>
        <div style="display: flex; flex-direction: column; gap: 0.7rem;">
            <div style="display: flex; align-items: flex-start; gap: 0.8rem;">
                <span style="color: #FF4D6D; font-weight: 700; min-width: 24px;">01</span>
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">Meta Ads API Pull</div>
                    <div style="color: #6B7394; font-size: 0.78rem;">Python → InstaPulse_Meta_API_Daily_Pull.ipynb</div>
                </div>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 0.8rem;">
                <span style="color: #FF4D6D; font-weight: 700; min-width: 24px;">02</span>
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">GA4 Daily Session Pull</div>
                    <div style="color: #6B7394; font-size: 0.78rem;">Google Analytics Data API → Excel</div>
                </div>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 0.8rem;">
                <span style="color: #FF4D6D; font-weight: 700; min-width: 24px;">03</span>
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">Attribution Reconciliation</div>
                    <div style="color: #6B7394; font-size: 0.78rem;">Meta + GA4 + Shopify → COD-adjusted ROAS</div>
                </div>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 0.8rem;">
                <span style="color: #FF4D6D; font-weight: 700; min-width: 24px;">04</span>
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">Client Report Generation</div>
                    <div style="color: #6B7394; font-size: 0.78rem;">Python + Node.js → .docx per client</div>
                </div>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 0.8rem;">
                <span style="color: #FF4D6D; font-weight: 700; min-width: 24px;">05</span>
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">Telegram Briefing</div>
                    <div style="color: #6B7394; font-size: 0.78rem;">Automated morning summary → Telegram Bot</div>
                </div>
            </div>
        </div>
        <div style="margin-top: 1.2rem; padding-top: 1rem; border-top: 1px solid #1E2230; font-size: 0.75rem; color: #3D4460;">
            Orchestrated via Windows Task Scheduler · Runs 7:00 AM IST daily
        </div>
    </div>
    """, unsafe_allow_html=True)

with a2:
    st.markdown("""
    <div style="background: #13161F; border: 1px solid #1E2230; border-radius: 14px; padding: 1.6rem;">
        <div style="font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #4ADE80; margin-bottom: 1rem;">Active Client Roster</div>
        <div style="display: flex; flex-direction: column; gap: 0.8rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.6rem 0; border-bottom: 1px solid #1A1E2C;">
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">Atharva Jaipur</div>
                    <div style="color: #6B7394; font-size: 0.75rem;">Cotton Kurtis · Own D2C Brand</div>
                </div>
                <span style="background: #0D2A1A; color: #4ADE80; padding: 3px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 600;">Owner</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.6rem 0; border-bottom: 1px solid #1A1E2C;">
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">Doriya Jaipur</div>
                    <div style="color: #6B7394; font-size: 0.75rem;">Ethnic Wear · Shopify Horizon</div>
                </div>
                <span style="background: #1A1E2C; color: #A0A8C0; padding: 3px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 600;">Client</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.6rem 0; border-bottom: 1px solid #1A1E2C;">
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">GemSpeak</div>
                    <div style="color: #6B7394; font-size: 0.75rem;">Gemstones · USA Meta Ads</div>
                </div>
                <span style="background: #1A1E2C; color: #A0A8C0; padding: 3px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 600;">Client</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.6rem 0; border-bottom: 1px solid #1A1E2C;">
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">IndigoTrend</div>
                    <div style="color: #6B7394; font-size: 0.75rem;">Fashion · Full Shopify Build</div>
                </div>
                <span style="background: #1A1E2C; color: #A0A8C0; padding: 3px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 600;">Client</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.6rem 0;">
                <div>
                    <div style="font-weight: 600; font-size: 0.88rem;">Yaviya</div>
                    <div style="color: #6B7394; font-size: 0.75rem;">D2C Fashion · Meta Ads</div>
                </div>
                <span style="background: #1A1E2C; color: #A0A8C0; padding: 3px 10px; border-radius: 20px; font-size: 0.72rem; font-weight: 600;">Client</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ─── FAQ ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">FAQ</div>', unsafe_allow_html=True)
st.markdown('<h2 style="margin-top: 0;">Common Questions</h2>', unsafe_allow_html=True)

with st.expander("❓ Are these affiliate links? Is this biased?"):
    st.markdown("""
    Yes, marked affiliate links earn me a commission at no extra cost to you. But I only list tools 
    I actively use or have deployed for clients managing real ad spend. I've excluded several 
    popular tools (like ClickFunnels) that I tested but don't use in practice.
    """)

with st.expander("🛒 I'm launching a D2C brand in India. Where do I start?"):
    st.markdown("""
    **Start with Shopify** (not WooCommerce, not custom) — the ecosystem for D2C in India is now 
    deeply integrated with Meta Ads, Shiprocket, and Razorpay. Use Hostinger for any 
    supplementary landing pages. For creatives, InVideo AI or Canva Pro depending on 
    whether you need video or static. I offer onboarding help via the contact form below.
    """)

with st.expander("📊 Can you manage my Meta Ads?"):
    st.markdown("""
    Yes. InstaPulse takes on select D2C clients in ethnic wear, fashion, jewellery, and 
    adjacent categories. I work with a single System User token pipeline for all clients, 
    with full attribution reconciliation (Meta + GA4 + Shopify), COD-adjusted ROAS tracking, 
    and daily automated reports. Min. ad spend: ₹1L/month. Reach out below.
    """)

with st.expander("🔧 Do I need to know Python to use your tools?"):
    st.markdown("""
    No. All the tools in this stack (Shopify, Hostinger, InVideo, Canva, SEMrush) are 
    no-code. My Python automation pipeline is for my own agency operations — it's not 
    a prerequisite to benefit from this stack. If you want to build something similar for 
    your own agency, I'm happy to share templates.
    """)

st.divider()

# ─── LEAD CAPTURE ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Get the SOP</div>', unsafe_allow_html=True)
st.markdown('<h2 style="margin-top: 0;">Download My 2026 D2C Scaling SOP</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #8890AA; margin-bottom: 1.5rem;">The exact checklist I run for every new client onboarding: Meta Pixel audit, GA4 setup, CAPI validation, campaign structure, and daily reporting pipeline.</p>', unsafe_allow_html=True)

lc1, lc2 = st.columns([2, 1])
with lc1:
    email = st.text_input("Your Email Address", placeholder="you@brand.com")
    brand = st.text_input("Your Brand / Store URL (optional)", placeholder="mybrand.myshopify.com")

with lc2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: #13161F; border: 1px solid #1E2230; border-radius: 10px; padding: 1.2rem; font-size: 0.82rem; color: #6B7394; line-height: 1.8;">
        <strong style="color: #A0A8C0;">SOP Includes:</strong><br>
        ✓ Meta Pixel + CAPI audit checklist<br>
        ✓ GA4 event tracking setup<br>
        ✓ Campaign structure template<br>
        ✓ Daily reporting automation guide<br>
        ✓ COD order exclusion logic
    </div>
    """, unsafe_allow_html=True)

if st.button("📨 Send Me the SOP →"):
    if email:
        st.success(f"✅ Got it! I'll send the SOP to **{email}** within 24 hours (IST).")
    else:
        st.warning("Please enter your email address first.")

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div style="margin-bottom: 0.5rem; font-family: 'Syne', sans-serif; font-size: 0.9rem; font-weight: 700; color: #E8EAF0;">
        ⚡ InstaPulse Agency
    </div>
    <div style="margin-bottom: 0.3rem;">
        Performance Marketing · Shopify Development · Python Analytics
    </div>
    <div>
        Jaipur, India · © 2026 InstaPulse · All affiliate links disclosed
    </div>
</div>
""", unsafe_allow_html=True)
