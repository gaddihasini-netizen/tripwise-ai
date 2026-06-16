import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="TripWise AI",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 TripWise AI")
st.subheader("Your AI Travel Planner")

api_key = st.text_input(
    "OpenAI API Key",
    type="password"
)

destination = st.text_input(
    "Destination",
    "Goa"
)

budget = st.selectbox(
    "Budget",
    ["Budget", "Standard", "Premium"]
)

style = st.selectbox(
    "Travel Style",
    ["Adventure", "Cultural", "Nature", "Luxury", "Family"]
)

travelers = st.number_input(
    "Travelers",
    min_value=1,
    value=2
)

if st.button("Generate Itinerary"):

    if not api_key:
        st.error("Enter OpenAI API Key")
        st.stop()

    with st.spinner("Planning your trip..."):

        client = OpenAI(api_key=api_key)

        prompt = f"""
Create a detailed travel itinerary.

Destination: {destination}
Budget: {budget}
Travel Style: {style}
Travelers: {travelers}

Include:
- Day-by-day plan
- Morning activities
- Afternoon activities
- Evening activities
- Estimated costs
- Food recommendations
- Travel tips
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        itinerary = response.choices[0].message.content

        st.markdown(itinerary)

        st.download_button(
            "Download Itinerary",
            itinerary,
            file_name="trip.txt"
        )
