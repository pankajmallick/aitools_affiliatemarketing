import streamlit as st

# 1. Page Config
st.set_page_config(page_title="2026 Media Buyer Stack", page_icon="📈")

# 2. Header / Authority Section
st.title("🚀 The 2026 Performance Marketing Stack")
st.markdown("""
*Curated by a Senior Media Buyer with 10+ years experience.*  
These tools currently drive my **4.0+ ROAS** campaigns.
""")

st.divider()

# 3. Product Columns (Affiliate Links)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🤖 AI Video Creator")
    st.image("https://via.placeholder.com/400x200?text=InVideo+AI") # Replace with real image
    st.write("Turn prompts into high-converting Meta Video Ads in seconds.")
    st.link_button("Try InVideo AI (Free Trial)", "https://your-affiliate-link-here.com")

with col2:
    st.subheader("⚙️ Marketing Automation")
    st.image("https://via.placeholder.com/400x200?text=Systeme.io")
    st.write("The all-in-one engine for your sales funnels and email loops.")
    st.link_button("Get Free Account", "https://your-systeme-link.com")

st.divider()

# 4. Authority/Trust Section
with st.expander("Why I trust these tools?"):
    st.write("""
    As a senior Performance Media Buyer, I don't like fluff. 
    I've tested 50+ AI tools this year; these are the only ones that actually 
    impact the bottom line.
    """)

# 5. Footer
st.caption("© 2026 Instapulse Agency. Some links are affiliate links.")