import streamlit as st
import datetime
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="TripWise AI - Ultimate Travel Workspace",
    page_icon="✈️",
    layout="wide"
)

# --- PREMIUM DYNAMIC THEME OVERRIDE ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 50%, #fce7f3 100%) !important;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%) !important;
        box-shadow: 5px 0px 15px rgba(0,0,0,0.2);
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] input, [data-testid="stSidebar"] select, [data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: #111827 !important;
    }
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
    .stButton>button {
        background: linear-gradient(90deg, #f43f5e 0%, #f97316 100%) !important;
        color: white !important;
        border: none !important;
        padding: 16px 32px !important;
        font-size: 1.1rem !important;
        font-weight: 800 !important;
        border-radius: 50px !important;
        box-shadow: 0 10px 25px rgba(244, 63, 94, 0.4) !important;
        transition: transform 0.2s ease;
    }
    .stButton>button:hover {
        transform: scale(1.03) translateY(-2px);
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 24px !important;
        padding: 35px !important;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08) !important;
        border: 2px solid #ffffff !important;
        margin-bottom: 25px;
    }
    
    /* Booking Link Quick Badges */
    .booking-pill {
        display: inline-block;
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        color: white !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        text-decoration: none !important;
        margin-top: 5px;
        margin-right: 8px;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.15);
        transition: all 0.2s ease;
    }
    .booking-pill:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 14px rgba(37, 99, 235, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar Control Input Panel
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.title("🏝️ TripWise Studio")
st.sidebar.markdown("Configure your trip logistics.")

destination = st.sidebar.text_input("📍 Destination Location", value="Goa")

col1, col2 = st.sidebar.columns(2)
with col1:
    start_date = st.sidebar.date_input("📅 Start Date", datetime.date.today())
with col2:
    end_date = st.sidebar.date_input("📅 End Date", datetime.date.today() + datetime.timedelta(days=2))

budget = st.sidebar.selectbox("💰 Budget Category", ["Budget", "Standard", "Premium"])
style = st.sidebar.selectbox("🏖️ Travel Style", ["Adventure", "Cultural", "Nature", "Luxury", "Family"])
travelers = st.sidebar.number_input("👥 Travelers Group Size", min_value=1, value=2)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.sidebar.button("✨ Click to Build Instantly!", use_container_width=True)

# Process Exact Selected Duration
duration = (end_date - start_date).days + 1
if duration <= 0:
    duration = 1

# 3. Main Dashboard Rendering Layout
st.markdown('<h1 class="super-title">✈️ TripWise AI Master</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your ultimate interactive visual dream getaway matrix workspace.</p>', unsafe_allow_html=True)

if generate_btn and destination:
    # High Fidelity Real-World Location Database Blueprint Mapping
    loc_clean = destination.strip().lower()
    
    if "goa" in loc_clean:
        spots = [
            {"name": "Calangute Beach & Water Trails", "desc": "Parasailing, jet skiing, and high-speed banana boat rides along the vibrant coastline."},
            {"name": "Basilica of Bom Jesus", "desc": "UNESCO World Heritage site showcasing stunning baroque architecture and deep rich history."},
            {"name": "Dudhsagar Waterfalls", "desc": "A majestic four-tiered white-water cascading wonder nestled in rich deciduous forests."},
            {"name": "Fontainhas Latin Quarter", "desc": "Walking trails through narrow winding streets lined with bright, colorful Portuguese villas."},
            {"name": "Anjuna Flea Market & Coastline Walk", "desc": "Vibrant bohemian street shopping, handicrafts, and live musical food shacks."},
            {"name": "Fort Aguada", "desc": "Seventeenth-century historical lighthouse fortress providing panoramic ocean viewscapes."}
        ]
        weather = "Tropical climate. Sunny coastal visibility with soft sea breezes. Peak outdoor comfort ranges from 7:00 AM to 11:00 AM and 4:30 PM to 8:00 PM."
        crowds = "High density patterns around famous north coast beaches between 2:00 PM and 6:30 PM. Visit historical heritage churches at opening hours to bypass tours."
    elif "pari" in loc_clean:
        spots = [
            {"name": "Eiffel Tower & Champ de Mars", "desc": "Iconic landmark observation deck experience paired with scenic green lawns."},
            {"name": "Louvre Museum Galleries", "desc": "Immense historical palace displaying world-class art masterpieces and relics."},
            {"name": "Montmartre & Sacré-Cœur", "desc": "Charming hilltop artist village paths leading to magnificent structural city views."},
            {"name": "Seine River Cruise Network", "desc": "Relaxing architectural historic boat transit highlighting iconic bridges and exhibits."},
            {"name": "Palace of Versailles", "desc": "Grand royal gardens, hall of mirrors, and luxury historical estate walking circuits."},
            {"name": "Musée d'Orsay", "desc": "Stunning historic railway station housing massive collections of legendary impressionist art."}
        ]
        weather = "Mild maritime conditions. Perfect afternoon walking visibility. Always pack a lightweight windbreaker layer and a portable compact umbrella."
        crowds = "Massive waiting lines across central art hubs between 11:00 AM and 3:30 PM. Pre-book skip-the-line museum tickets online weeks in advance."
    else:
        # Generic Custom Dynamic Generation Fallback Engine
        spots = [
            {"name": f"Central {destination} Discovery Hub", "desc": "Immersive local exploration circuit uncovering core landmarks and community heritage."},
            {"name": f"Historic {destination} Landmark Trail", "desc": "Guided walking tour detailing architectural transformations and local storytelling."},
            {"name": f"Scenic {destination} Panoramic Outlook", "desc": "Stunning natural vista point perfect for afternoon photography and landscape treks."},
            {"name": f"The Local {destination} Arts Market", "desc": "Charming street bazaar featuring artisanal culinary treats, crafts, and live displays."},
            {"name": f"Hidden {destination} Nature Reserve", "desc": "Tranquil outdoor sanctuary containing curated wildlife trails and relaxing pathways."}
        ]
        weather = "Favorable seasonal parameters. Standard clear daytime sky conditions with comfortable evening temperature cooling cycles."
        crowds = "Moderate density lines around main city plazas between noon and late afternoon. Target early morning windows for completely clear photogenic frames."

    # Dynamic Budget Calculation Matrices (Configured in Indian Rupees - INR)
    base_modifier = 2500 if budget == "Budget" else (6500 if budget == "Standard" else 16000)
    total_val = duration * base_modifier * travelers

    left_side, right_side = st.columns([6, 4])
    
    with left_side:
        st.markdown(f"""
        <div class="glass-card">
            <h2 style="color:#1e3a8a; margin-top:0;">📋 Custom Day-by-Day Agenda: {destination}</h2>
            <p><i>Generated seamlessly for **{travelers} travelers** pursuing a **{style}** itinerary across **{duration} Days**.</i></p>
            <hr style="border-color:#e2e8f0;">
        """, unsafe_allow_html=True)
        
        # DYNAMIC DAY LOOP GENERATION (Builds out exact duration user inputs)
        for d in range(1, duration + 1):
            spot_m = spots[(d * 3 - 3) % len(spots)]
            spot_a = spots[(d * 3 - 2) % len(spots)]
            spot_e = spots[(d * 3 - 1) % len(spots)]
            
            st.markdown(f"""
            <h3 style="color:#8b5cf6;">🌅 Day {d}: Premium {style} Track</h3>
            <ul>
                <li style="margin-bottom: 15px;"><b>Morning (09:00 AM - 12:30 PM)</b>:<br>
                    <u>{spot_m['name']}</u> — {spot_m['desc']}<br>
                    <span style="color:#10b981; font-weight:600;">Est. Cost: ₹{int(base_modifier*0.15)}</span> | Duration: 3.5 Hours<br>
                    <a class="booking-pill" href="https://www.google.com/search?q=book+entry+tickets+for+{spot_m['name'].replace(' ', '+')}" target="_blank">🎟️ Instant Pass Booking</a>
                </li>
                <li style="margin-bottom: 15px;"><b>Afternoon (01:30 PM - 05:00 PM)</b>:<br>
                    <u>{spot_a['name']}</u> — {spot_a['desc']}<br>
                    <span style="color:#10b981; font-weight:600;">Est. Cost: ₹{int(base_modifier*0.25)}</span> | Duration: 3.5 Hours<br>
                    <a class="booking-pill" href="https://www.google.com/search?q=reserve+tours+for+{spot_a['name'].replace(' ', '+')}" target="_blank">🧗 Reserve Activity Ride</a>
                </li>
                <li style="margin-bottom: 15px;"><b>Evening (06:30 PM - 10:00 PM)</b>:<br>
                    <u>{spot_e['name']}</u> — {spot_e['desc']}<br>
                    <span style="color:#10b981; font-weight:600;">Est. Cost: ₹{int(base_modifier*0.20)}</span> | Duration: 3.5 Hours<br>
                    <a class="booking-pill" href="https://www.google.com/search?q=top+restaurants+near+{spot_e['name'].replace(' ', '+')}" target="_blank">🍲 Book Dining Table</a>
                </li>
            </ul>
            <hr style="border-color:#e2e8f0;">
            """, unsafe_allow_html=True)
            
        st.markdown(f"""
            <h3 style="color:#f97316;">☀️ Climate & Crowd Tracking Insights</h3>
            <p><b>Real-Life Weather Advice</b>: {weather}</p>
            <p><b>Peak Crowd Analysis</b>: {crowds}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with right_side:
        # Global Booking Gateway Panel
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top:0; color:#1e3a8a;'>⚡ Express Booking Gateway</h3>", unsafe_allow_html=True)
        st.caption("Secure your major fleet logistics and hospitality stays instantly.")
        
        book_col1, book_col2 = st.columns(2)
        with book_col1:
            st.markdown(f'<a class="booking-pill" style="display:block; text-align:center; padding:10px;" href="https://www.google.com/search?q=flights+to+{destination}" target="_blank">✈️ Book Roundtrip Flights</a>', unsafe_allow_html=True)
        with book_col2:
            st.markdown(f'<a class="booking-pill" style="display:block; text-align:center; padding:10px; background:linear-gradient(90deg, #ec4899, #f43f5e);" href="https://www.google.com/search?q=best+hotels+stay+in+{destination}" target="_blank">🏨 Book Luxury Stays</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top:0; color:#1e3a8a;'>📊 Budget Allocation Breakdown</h3>", unsafe_allow_html=True)
        
        st.metric(label="Calculated Combined Itinerary Value (INR)", value=f"₹{total_val:,.2f}", delta=f"{budget} Configuration")
        
        # Real Interactive Bar Chart Updates using Indian Rupees
        chart_data = pd.DataFrame({
            'Expense Categories': ['Accommodation', 'Culinary & Food', 'Transit Systems', 'Activity Tickets'],
            'Cost Allocations (₹)': [total_val * 0.45, total_val * 0.25, total_val * 0.15, total_val * 0.15]
        })
        st.bar_chart(data=chart_data, x='Expense Categories', y='Cost Allocations (₹)')
        
        st.markdown("<hr style='border-color:#e2e8f0;'>", unsafe_allow_html=True)
        st.markdown("### 📸 Destination Photo Inspiration", unsafe_allow_html=True)
        
        # Match dynamic landscape imagery to destination
        img_src = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600" if "goa" in loc_clean else ("https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=600" if "pari" in loc_clean else "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=600")
        st.image(img_src, caption=f"Dynamic background snapshot matching your customized trip layout.", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # High-impact welcoming workspace presentation screen
    st.markdown("""
        <div class="glass-card">
            <h2 style="color: #1e3a8a; margin-top:0; font-size:1.8rem;">🏝️ Welcome to Your Premium Master Travel Space</h2>
            <p style="color: #475569; font-size:1.1rem; line-height:1.7;">
                The travel workspace engine is now fully dynamic. Simply configure your desired target location, exact dates, 
                group count, and travel parameters on the deep-indigo command center to your left. 
                The system will automatically run full layout logic loops mapping out <b>as many days as you choose</b> instantly, tracked smoothly in <b>Indian Rupees (₹)</b> with built-in instant direct booking shortcuts!
            </p>
            <div style="display: flex; gap: 15px; margin-top: 30px; justify-content: space-between; flex-wrap: wrap;">
                <img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=400" style="width: 31%; border-radius:16px; height:180px; object-fit:cover;">
                <img src="https://images.unsplash.com/photo-1506929562872-bb421503ef21?q=80&w=400" style="width: 31%; border-radius:16px; height:180px; object-fit:cover;">
                <img src="https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=400" style="width: 31%; border-radius:16px; height:180px; object-fit:cover;">
            </div>
        </div>
    """, unsafe_allow_html=True)
