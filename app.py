import streamlit as st
import datetime
import pandas as pd
import plotly.express as px
from openai import OpenAI
from fpdf import FPDF

# Page Config
st.set_page_config(page_title="TripWise AI", page_icon="✈️", layout="wide")

st.title("✈️ TripWise AI Planner")
st.caption("Generate your custom day-by-day travel itinerary in seconds.")

# API Key Input right on the main page so it never fails
api_key_input = st.text_input("🔑 Enter your OpenAI API Key (starts with sk-)", type="password")

# Sidebar for Inputs
st.sidebar.title("🗺️ Trip Parameters")
destination = st.sidebar.text_input("📍 Destination", placeholder="e.g. Goa, Paris")
start_date = st.sidebar.date_input("📅 Start Date", datetime.date.today())
end_date = st.sidebar.date_input("📅 End Date", datetime.date.today() + datetime.timedelta(days=3))
budget = st.sidebar.selectbox("💰 Budget", ["Budget", "Standard", "Premium"])
style = st.sidebar.selectbox("🏖️ Style", ["Adventure", "Cultural", "Nature", "Luxury", "Family"])
travelers = st.sidebar.number_input("👥 Travelers", min_value=1, value=1)

generate_btn = st.sidebar.button("✨ Generate Itinerary", use_container_width=True)

if generate_btn:
    if not api_key_input.strip():
        st.error("Please enter your OpenAI API key in the input field above first!")
    elif not destination.strip():
        st.error("Please enter a destination!")
    else:
        duration = (end_date - start_date).days + 1
        client = OpenAI(api_key=api_key_input.strip())
        
        with st.spinner("Planning your trip..."):
            try:
                # 1. AI Generation
                prompt = f"Create a day-by-day travel itinerary for {duration} days in {destination}. Budget: {budget}, Style: {style}, Travelers: {travelers}. Provide Morning, Afternoon, and Evening activities with estimated costs and local tips. Return response in clean markdown format."
                
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                itinerary_text = response.choices[0].message.content
                
                # 2. Display Layout
                col1, col2 = st.columns([6, 4])
                
                with col1:
                    st.subheader("📋 Your Custom Itinerary")
                    st.markdown(itinerary_text)
                    
                    # Download Buttons
                    st.download_button("📝 Download TXT Document", data=itinerary_text, file_name="itinerary.txt", mime="text/plain")
                
                with col2:
                    st.subheader("📊 Estimated Cost Breakdown")
                    # Simple automated visual calculation based on budget tier chosen
                    mult = 50 if budget == "Budget" else (120 if budget == "Standard" else 300)
                    base_cost = duration * mult * travelers
                    
                    chart_data = pd.DataFrame({
                        "Category": ["Accommodation", "Food", "Transport", "Activities"],
                        "Cost ($)": [base_cost * 0.4, base_cost * 0.3, base_cost * 0.15, base_cost * 0.15]
                    })
                    
                    st.dataframe(chart_data, hide_index=True, use_container_width=True)
                    st.metric(label="Total Estimated Cost", value=f"${base_cost:,.2f}")
                    
                    fig = px.pie(chart_data, values="Cost ($)", names="Category", title="Budget Distribution")
                    st.plotly_chart(fig, use_container_width=True)
                    
            except Exception as e:
                st.error(f"API Error: {str(e)}")
