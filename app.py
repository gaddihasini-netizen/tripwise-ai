import streamlit as st
import datetime
import pandas as pd

# 1. Force Page Refresh Configurations
st.set_page_config(
    page_title="TripWise AI - Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# Reset session states cleanly
if "trip_ready" not in st.session_state:
    st.session_state.trip_ready = False

# --- ULTRA-COLOURFUL BRIGHT THEME OVERRIDE ---
st.markdown("""
    <style>
    /* Vibrant Full Page Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 50%, #fce7f3 100%) !important;
    }
    
    /* Bright Pop Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%) !important;
        box-shadow: 5px 0px 15px rgba(0,0,0,0.2);
    }
    
    /* Sidebar Text Highlights */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    /* Neon Glowing Main Title */
    .super-title {
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #ec4899, #8b5cf6, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    
    .subtitle {
        font-size: 1.3rem;
        color: #475569;
        font-weight: 500;
        margin-bottom: 30px;
    }

    /* Vibrant Pink/Orange Fire Action Button */
    .stButton>button {
        background: linear-gradient(90deg, #f43f5e 0%, #f97316 100%) !important;
        color: white !important;
        border: none !important;
        padding: 16px 32px !important;
        font-size: 1.1rem !important;
        font-weight: 800 !important;
        border-radius: 50px !important;
        box-shadow: 0 10px 25px rgba(244, 63, 94, 0.4) !important;
        cursor: pointer;
        transition: transform 0.2s ease;
    }
    .stButton>button:hover {
        transform: scale(1.03) translateY(-2px);
    }
    
    /* Clean Content Visual Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 24px !important;
        padding: 35px !important;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08) !important;
        border: 2px solid #ffffff !important;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Control Input Sidebar
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.title("🏝️ TripWise Studio")
st.sidebar.markdown("Set your customized escape matrices below.")

destination = st.sidebar.text_input("📍 Destination Location", value="Goa")

col1, col2 = st.sidebar.columns(2)
with col1:
    start_date = st.sidebar.date_input("📅 Start Date", datetime.date.today())
with col2:
    end_date = st.sidebar.date_input("📅 End Date", datetime.date.today() + datetime.timedelta(days=3))

budget = st.sidebar.selectbox("💰 Budget Category", ["Budget", "Standard", "Premium"])
style = st.sidebar.selectbox("🏖️ Travel Style", ["Adventure", "Cultural", "Nature", "Luxury", "Family"])
travelers = st.sidebar.number_input("👥 Travelers Group Size", min_value=1, value=2)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.sidebar.button("✨ Click to Build Instantly!", use_container_width=True)

if generate_btn:
    st.session_state.trip_ready = True

# 3. Main Stage Content View Screen
st.markdown('<h1 class="super-title">✈️ TripWise AI Master</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your ultimate interactive visual dream getaway matrix workspace.</p>', unsafe_allow_html=True)

if st.session_state.trip_ready and destination:
    duration = (end_date - start_date).days + 1
    if duration <= 0:
        duration = 3
        
    mult = 70 if budget == "Budget" else (160 if budget == "Standard" else 400)
    total_val = duration * mult * travelers

    # Dynamic Layout Split
    left_side, right_side = st.columns([6, 4])
    
    with left_side:
        st.markdown(f"""
        <div class="glass-card">
            <h2 style="color:#1e3a8a; margin-top:0;">📋 Custom Day-by-Day Agenda: {destination}</h2>
            <p><i>Generated seamlessly for <b>{travelers} travelers</b> looking for a <b>{style}</b> timeline.</i></p>
            <hr style="border-color:#e2e8f0;">
            <h3>🌅 Day 1: Perfect Arrival & Kickoff</h3>
            <ul>
                <li><b>Morning</b>: Explore historic local architecture districts and morning markets. (Est. ${int(mult*0.2)})</li>
                <li><b>Afternoon</b>: Move out on a specialized <b>{style}</b> tour across central beachways or paths. (Est. ${int(mult*0.3)})</li>
                <li><b>Evening</b>: Dinner at a beach shacks/bazaars with authentic local food pairings. (Est. ${int(mult*0.15)})</li>
            </ul>
            <h3>☀️ Day 2: Peak Exploration Trails</h3>
            <ul>
                <li><b>Morning</b>: Sunrise trek/coastal walk before density levels surge up. (Est. ${int(mult*0.1)})</li>
                <li><b>Afternoon</b>: Guided local excursions, water trails, or museum entries. (Est. ${int(mult*0.4)})</li>
                <li><b>Evening</b>: Premium sunset cruise / observation points and lounge markets. (Est. ${int(mult*0.2)})</li>
            </ul>
            <hr style="border-color:#e2e8f0;">
            <h3>⛅ Weather & Crowds Summary</h3>
            <p><b>Expected Climate</b>: Clean skies, warm afternoon sun, soft breeze tracks.</p>
            <p><b>Crowd Management Track</b>: High concentration zones between 1:00 PM and 4:00 PM. Move early to bypass long registration lines.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with right_side:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top:0; color:#1e3a8a;'>📊 Budget Allocation Breakdown</h3>", unsafe_allow_html=True)
        
        # Display Metric Cards
        st.metric(label="Calculated Profile Total Expense", value=f"${total_val:,.2f}", delta=f"{budget} Status")
        
        # Create Native Streamlit Interactive Bar Chart
        chart_data = pd.DataFrame({
            'Expense Streams': ['Hotel Stay', 'Culinary Routes', 'Transit Logistics', 'Adventures'],
            'Cost Allocations ($)': [total_val * 0.40, total_val * 0.25, total_val * 0.15, total_val * 0.20]
        })
        st.bar_chart(data=chart_data, x='Expense Streams', y='Cost Allocations ($)')
        
        st.markdown("<hr style='border-color:#e2e8f0;'>", unsafe_allow_html=True)
        st.markdown("### 📸 Visual Exploration Capture", unsafe_allow_html=True)
        # Display dynamic high-res gorgeous travel imagery matching the traveler profile style
        img_src = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600" if style != "Nature" else "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?q=80&w=600"
        st.image(img_src, caption=f"Dynamic background view matching a {style} vacation profile.", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # High-impact, colorful welcoming splash layout cards
    st.markdown("""
        <div class="glass-card">
            <h2 style="color: #1e3a8a; margin-top:0; font-size:1.8rem;">🏝️ Welcome to Your Premium Master Travel Space</h2>
            <p style="color: #475569; font-size:1.1rem; line-height:1.7;">
                The backend parameters are updated completely. No external authentications or API keys are required. 
                Simply input your vacation criteria inside the custom deep-indigo workspace block on the left panel, 
                then press <b>Click to Build Instantly</b> to render gorgeous schedules and data graphs live!
            </p>
            <div style="display: flex; gap: 15px; margin-top: 30px; justify-content: space-between; flex-wrap: wrap;">
                <img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=400" style="width: 31%; border-radius:16px; height:180px; object-fit:cover; box-shadow:0 8px 20px rgba(0,0,0,0.1);">
                <img src="https://images.unsplash.com/photo-1506929562872-bb421503ef21?q=80&w=400" style="width: 31%; border-radius:16px; height:180px; object-fit:cover; box-shadow:0 8px 20px rgba(0,0,0,0.1);">
                <img src="https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=400" style="width: 31%; border-radius:16px; height:180px; object-fit:cover; box-shadow:0 8px 20px rgba(0,0,0,0.1);">
            </div>
        </div>
    """, unsafe_allow_html=True)
