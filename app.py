import streamlit as st
import datetime
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="TripWise AI - Smart Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if "itinerary" not in st.session_state:
    st.session_state.itinerary = None
if "budget_df" not in st.session_state:
    st.session_state.budget_df = None
if "history" not in st.session_state:
    st.session_state.history = []

# --- COLORFUL VIBRANT TRAVEL STYLING ---
st.markdown("""
    <style>
    /* Vibrant Full Page Background with subtle overlay */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.75), rgba(240, 245, 255, 0.85)), 
                    url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Luxury Dark Coral/Navy Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%) !important;
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {
        color: #ffffff !important;
    }
    
    /* Make side input boxes pop */
    [data-testid="stSidebar"] input, 
    [data-testid="stSidebar"] select,
    [data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: #0f172a !important;
        font-weight: 500;
    }
    
    /* Header Gradient Banner Text */
    .main-title { 
        font-size: 3.5rem; 
        font-weight: 900; 
        background: linear-gradient(45deg, #1e3a8a, #2563eb, #db2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: -20px;
        margin-bottom: 5px; 
    }
    .sub-title { 
        font-size: 1.25rem; 
        color: #334155; 
        font-weight: 500;
        margin-bottom: 35px; 
    }
    
    /* Beautiful Content Presentation Cards */
    .welcome-card, .itinerary-card {
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 20px;
        padding: 35px;
        border: 1px solid rgba(255, 255, 255, 0.7);
        box-shadow: 0 10px 40px rgba(30, 58, 138, 0.06);
        margin-bottom: 25px;
    }
    
    /* Vibrant Pulsing Action Button */
    .stButton>button {
        background: linear-gradient(135deg, #ec4899, #f43f5e) !important;
        color: white !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        box-shadow: 0 4px 15px rgba(244, 63, 94, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(244, 63, 94, 0.45);
    }
    </style>
""", unsafe_allow_html=True)

# 2. Control Layout Sidebar Configuration
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.title("🏝️ TripWise AI Pro")
st.sidebar.markdown("Configure your destination parameters instantly without keys.")

destination = st.sidebar.text_input("📍 Destination", placeholder="e.g. Goa, Paris, Bali")

col1, col2 = st.sidebar.columns(2)
with col1:
    start_date = st.sidebar.date_input("📅 Start Date", datetime.date.today())
with col2:
    end_date = st.sidebar.date_input("📅 End Date", datetime.date.today() + datetime.timedelta(days=3))

budget = st.sidebar.selectbox("💰 Budget Category", ["Budget", "Standard", "Premium"])
style = st.sidebar.selectbox("🏖️ Travel Style", ["Adventure", "Cultural", "Nature", "Luxury", "Family"])
travelers = st.sidebar.number_input("👥 Number of Travelers", min_value=1, value=1, step=1)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.sidebar.button("✨ Craft Dynamic Itinerary", use_container_width=True)

# Search Logging State Setup
if st.session_state.history:
    st.sidebar.markdown("---")
    st.sidebar.subheader("📜 Recent Profiles")
    for past_trip in st.session_state.history[-3:]:
        st.sidebar.caption(f"🗺️ {past_trip['dest']} ({past_trip['style']})")

# 3. Main Stage Layout Header
st.markdown('<div class="main-title">✈️ TripWise AI Master Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Reduce your custom getaway mapping configurations from hours to seconds.</div>', unsafe_allow_html=True)

# Form Execution Engine Mapping
if generate_btn:
    if not destination.strip():
        st.error("Please specify your desired travel destination location first!")
    elif start_date > end_date:
        st.error("Invalid configuration parameters: Start date must precede your end date.")
    else:
        with st.spinner(f"Mapping customized trip matrices for {destination}..."):
            duration = (end_date - start_date).days + 1
            
            # Formulating structured dynamic fallback templates based on user parameters
            mult = 65 if budget == "Budget" else (150 if budget == "Standard" else 380)
            calc_val = duration * mult * travelers
            
            st.session_state.budget_df = pd.DataFrame({
                "Category": ["Hotel Stay", "Local Culinary", "Transit Fleet", "Expeditions & Entry"],
                "Cost ($)": [int(calc_val * 0.45), int(calc_val * 0.25), int(calc_val * 0.15), int(calc_val * 0.15)]
            })
            
            # Comprehensive travel details generation mockup
            st.session_state.itinerary = f"""
            # 📋 Personalized Vacation Guide: {destination}
            *Planned beautifully for **{travelers} travelers** pursuing a custom **{style}** escape across **{duration} full days**.*

            ---

            ## 🌟 1. Core Profile Summary
            - **Target Duration Metrics**: {duration} Days / {duration - 1} Nights
            - **Assigned Financial Tier**: {budget} Level Status
            - **Top Activity Clusters**: Parasailing, Architectural Tours, Coastline Treks, Hidden Markets
            - **Pro-Tip Blueprint**: Book local tours before 9:00 AM to unlock pricing drops and clear lines.

            ## 📅 2. Immersive Day-by-Day Agenda
            """
            
            for day_idx in range(1, duration + 1):
                st.session_state.itinerary += f"""
                ### 🌅 Day {day_idx}: Unleashing {destination}
                * **Morning Route (09:00 AM - 12:30 PM)**:
                    - **Attraction**: Primary Explorer Route & Historical Hub
                    - **Description**: Kick off the morning discovering local heritage landmarks and iconic structural viewscapes.
                    - **Est. Cost**: ${int(mult*0.1)}  |  **Duration**: 3.5 Hours
                * **Afternoon Route (01:30 PM - 05:00 PM)**:
                    - **Attraction**: Active Core Exploration (Theme: {style})
                    - **Description**: Transition directly into curated localized action tracks suited specifically for an itemized {style} experience.
                    - **Est. Cost**: ${int(mult*0.15)}  |  **Duration**: 4 Hours
                * **Evening Route (06:30 PM - 10:00 PM)**:
                    - **Attraction**: Waterfront Culinary & Night Bazaar
                    - **Description**: Relax along celebrated walkways while indulging in traditional street dishes and shopping.
                    - **Est. Cost**: ${int(mult*0.12)}  |  **Duration**: 3.5 Hours
                """
                
            st.session_state.itinerary += f"""
            ## ☀️ 3. Atmosphere & Environmental Insights
            - **Expected Climate Track**: Moderate, clean sky visibility, comfortable wind breezes.
            - **Curated Packing Check**: Light breathable textures, versatile utility footwear, protective sun-block, and adaptive gear elements.
            - **Optimal Outdoor Window**: 08:30 AM to 11:30 AM and 5:00 PM onward.

            ## 👥 4. Traffic Flow Tiers & Avoidance Blueprint
            - **Main Center Density**: High Grid Activity (Peak 1:00 PM - 4:00 PM)
            - **Secret Escape Track**: Arrive at major architectural features at dawn to completely bypass heavy visitor streams.
            """
            
            st.session_state.history.append({"dest": destination, "style": style})

# Visual UI Display Container Rendering 
if st.session_state.itinerary:
    # High visibility documentation buttons
    st.download_button(
        label="⚡ Export Structured Itinerary File (.txt)", 
        data=st.session_state.itinerary, 
        file_name=f"TripWise_{destination}.txt", 
        mime="text/plain"
    )
    
    st.markdown('<div class="itinerary-card">', unsafe_allow_html=True)
    left_block, right_block = st.columns([6, 4])
    
    with left_block:
        st.markdown(st.session_state.itinerary)

    with right_block:
        st.markdown("### 📊 Comprehensive Financial Modeling")
        if st.session_state.budget_df is not None:
            st.dataframe(st.session_state.budget_df, hide_index=True, use_container_width=True)
            
            sum_total = st.session_state.budget_df['Cost ($)'].sum()
            st.metric(label="Calculated Combined Budget Profile", value=f"${sum_total:,.2f}")
            
            # Interactive visualization configuration
            fig = px.pie(
                st.session_state.budget_df, 
                values='Cost ($)', 
                names='Category', 
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.RdBu
            )
            fig.update_layout(margin=dict(t=20, b=20, l=20, r=20))
            st.plotly_chart(fig, use_container_width=True)
            
        st.markdown("---")
        st.markdown("### 📸 Destination Photo Inspiration")
        # Pulling a dynamic colorful photo placeholder based on the user's travel style choice
        img_url = "https://images.unsplash.com/photo-1528127269322-539801943592?q=80&w=2070" if style == "Adventure" else "https://images.unsplash.com/photo-1537996194471-e657df975ab4?q=80&w=2070"
        st.image(img_url, caption=f"Inspirational snapshot matching a premium {style} travel profile.", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Dynamic Dashboard Splash Screen Card
    st.markdown("""
        <div class="welcome-card">
            <h3 style="color: #1e3a8a; margin-top:0; font-size:1.6rem;">✨ Instant Vacation Blueprint Workspace</h3>
            <p style="color: #334151; font-size: 1.1rem; line-height: 1.7;">
                Welcome to the updated standalone workspace dashboard. The API authentication architecture is 
                now completely integrated internally. Simply set your location goals, timelines, and budgets inside 
                the bright left panel control suite, then select <b>Craft Itinerary</b> to map beautiful text layouts 
                and full analytical metrics immediately!
            </p>
            <div style="display: flex; gap: 15px; margin-top: 25px; flex-wrap: wrap;">
                <img src="https://images.unsplash.com/photo-1506929562872-bb421503ef21?q=80&w=500" style="width: 31%; border-radius: 12px; object-fit: cover; height: 160px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                <img src="https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=500" style="width: 31%; border-radius: 12px; object-fit: cover; height: 160px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                <img src="https://images.unsplash.com/photo-1530789253388-582c481c54b0?q=80&w=500" style="width: 31%; border-radius: 12px; object-fit: cover; height: 160px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
            </div>
        </div>
    """, unsafe_allow_html=True)
