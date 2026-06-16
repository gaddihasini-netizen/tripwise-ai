```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="TripWise Travel",
    page_icon="✈️",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#E0F7FA,#FFFFFF);
}

.hero {
    background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size: cover;
    background-position: center;
    padding: 120px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}

.hero h1{
    font-size:60px;
}

.hero p{
    font-size:24px;
}

div[data-testid="stMetric"] {
    background-color:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.stButton>button{
    background:#00ACC1;
    color:white;
    border:none;
    border-radius:10px;
    padding:12px 25px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# HERO SECTION
# ----------------------------

st.markdown("""
<div class="hero">
    <h1>✈️ TripWise Travel</h1>
    <p>Plan Beautiful Trips In Seconds</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# POPULAR DESTINATIONS
# ----------------------------

st.subheader("🌍 Popular Destinations")

c1, c2, c3 = st.columns(3)

with c1:
    st.image(
        "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86",
        use_container_width=True
    )
    st.markdown("### Goa")

with c2:
    st.image(
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        use_container_width=True
    )
    st.markdown("### Bali")

with c3:
    st.image(
        "https://images.unsplash.com/photo-1493558103817-58b2924bce98",
        use_container_width=True
    )
    st.markdown("### Dubai")

st.divider()

# ----------------------------
# USER INPUTS
# ----------------------------

st.subheader("🧳 Plan Your Trip")

col1, col2 = st.columns(2)

with col1:
    destination = st.text_input(
        "Destination",
        "Goa"
    )

    budget = st.selectbox(
        "Budget",
        [
            "Budget",
            "Standard",
            "Premium"
        ]
    )

with col2:
    style = st.selectbox(
        "Travel Style",
        [
            "Adventure",
            "Nature",
            "Luxury",
            "Cultural",
            "Family"
        ]
    )

    travelers = st.number_input(
        "Travelers",
        min_value=1,
        value=2
    )

days = st.slider(
    "Trip Duration (Days)",
    1,
    10,
    3
)

generate = st.button("🚀 Generate Trip")

# ----------------------------
# GENERATE TRIP
# ----------------------------

if generate:

    st.success("Trip Generated Successfully!")

    st.header(f"📍 {destination} Itinerary")

    for day in range(1, days + 1):

        st.markdown(f"## Day {day}")

        st.markdown("""
### 🌅 Morning
Explore popular attractions and local cafes.

### ☀️ Afternoon
Sightseeing and photography spots.

### 🌙 Evening
Dinner, shopping and nightlife.
""")

    st.divider()

    st.header("💰 Budget Breakdown")

    if budget == "Budget":
        costs = [12000, 6000, 3000, 4000]

    elif budget == "Standard":
        costs = [25000, 12000, 7000, 9000]

    else:
        costs = [50000, 20000, 15000, 18000]

    df = pd.DataFrame({
        "Category": [
            "Accommodation",
            "Food",
            "Transport",
            "Activities"
        ],
        "Cost (₹)": costs
    })

    st.dataframe(
        df,
        use_container_width=True
    )

    total = sum(costs)

    m1, m2, m3 = st.columns(3)

    m1.metric("💵 Total Budget", f"₹{total:,}")
    m2.metric("👥 Travelers", travelers)
    m3.metric("📅 Duration", f"{days} Days")

    fig = px.pie(
        df,
        values="Cost (₹)",
        names="Category",
        title="Trip Cost Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.header("☀️ Weather Insights")

    st.info("""
Expected Weather: Warm and Sunny

Best Outdoor Hours:
• 7 AM – 11 AM
• 4 PM – 7 PM

Packing Suggestions:
• Sunglasses
• Sunscreen
• Comfortable Shoes
• Water Bottle
""")

    st.divider()

    st.header("👥 Crowd Prediction")

    crowd_df = pd.DataFrame({
        "Location":[
            "Beach Area",
            "Market Area",
            "Historic Sites"
        ],
        "Crowd Level":[
            "High",
            "Medium",
            "Low"
        ]
    })

    st.table(crowd_df)

    st.warning(
        "Visit major attractions before 9 AM to avoid crowds."
    )

    st.divider()

    st.header("✨ Travel Tips")

    st.success("🌴 Start your day early.")
    st.info("🍜 Try local food markets.")
    st.warning("🚕 Book transport in advance.")
    st.success("📸 Carry a power bank for photos.")

    itinerary_text = f"""
TripWise Travel Plan

Destination: {destination}
Travel Style: {style}
Budget: {budget}
Travelers: {travelers}
Duration: {days} Days

Have an amazing trip!
"""

    st.download_button(
        "📥 Download Itinerary",
        itinerary_text,
        file_name="TripWise_Itinerary.txt"
    )
```
