import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import google.generativeai as genai  # Gemini

# --- PAGE CONFIG ---
st.set_page_config(page_title="COIN50 Index", layout="wide")

# --- THEME SWITCH ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

mode = st.radio("🌙 Theme Mode:", ["🌞 Light", "🌙 Dark"], horizontal=True)
st.session_state.dark_mode = mode == "🌙 Dark"

if st.session_state.dark_mode:
    st.markdown("""
        <style>
        .main, body, .block-container {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        </style>
    """, unsafe_allow_html=True)

# --- TITLE ---
st.markdown("""
    <h1 style='text-align: center;'>From Code to Coin 💻🪙🔗</h1>
    <p style='text-align: center; color: grey;'>Your Gateway to Understanding the Coinbase 50 Index</p>
""", unsafe_allow_html=True)

# --- TABS (REORDERED) ---
tab1, tab2, tab3, tab4 = st.tabs(["Prediction and Insights", "Charts", "Chatbot", "Contact"])

# --- TAB 1: Prediction and Insights ---
tab1.subheader("📈 Prediction and Insights")

# OVERVIEW SECTION
tab1.markdown("### 🧾 Overview (Summary)")
tab1.markdown("""
The **COIN50 Index** tracks the top 50 cryptocurrencies on Coinbase, weighted by market cap and liquidity.  
It offers a diversified view of the digital asset landscape, rebalanced quarterly to stay aligned with market trends.  
It includes filters to avoid illiquid or overly volatile assets, and caps large positions to ensure diversification.
""")

# MOCK DATA CHART
dates = pd.date_range(start='2023-01-01', periods=100)
index_values = np.cumsum(np.random.normal(loc=0.1, scale=1.0, size=100)) + 100
df_trend = pd.DataFrame({"Date": dates, "Coinbase50_Index": index_values})
fig = px.line(df_trend, x="Date", y="Coinbase50_Index", title="Coinbase 50 Index Trend", markers=True)
tab1.plotly_chart(fig, use_container_width=True)

# --- TAB 2: Charts ---
tab2.subheader("📊 Market Cap Distribution (Mock Data)")
coins = [
    {"name": "Bitcoin", "weight": 50.30},
    {"name": "Ethereum", "weight": 22.69},
    {"name": "XRP", "weight": 9.37},
    {"name": "Solana", "weight": 5.91},
    {"name": "Dogecoin", "weight": 2.12},
    {"name": "Cardano", "weight": 1.76},
    {"name": "Chainlink", "weight": 0.67},
    {"name": "Avalanche", "weight": 0.64},
    {"name": "Stellar Lumen", "weight": 0.61},
    {"name": "Bitcoin Cash", "weight": 0.59},
]
coin_names = [coin["name"] for coin in coins]
weights = [coin["weight"] for coin in coins]
fig_bar = px.bar(x=coin_names, y=weights, labels={"x": "Coin", "y": "Weight (%)"}, title="Coin Weights in Index")
tab2.plotly_chart(fig_bar, use_container_width=True)

# --- TAB 3: Chatbot (Gemini) ---
tab3.subheader("🤖 Gemini-Powered Crypto Chatbot")

API_KEY = "AIzaSyA2R5r3D0CkyWQd3nf3FKkAVeDAFswJzEM"  # حطي مفتاحك الصحيح هنا
genai.configure(api_key=API_KEY)

try:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
except Exception as e:
    tab3.error(f"❌ Model Load Error: {e}")

user_input = tab3.text_input("Ask me anything about cryptocurrency (e.g., Bitcoin, Ethereum, blockchain):")

if user_input:
    with tab3.spinner("Thinking with Gemini..."):
        try:
            response = model.generate_content(user_input)
            tab3.success("🤖 " + response.text)
        except Exception as e:
            if "quota" in str(e).lower():
                tab3.error("⚠️ You've exceeded your Gemini API quota. Try again later or upgrade your plan.")
            elif "API key not valid" in str(e):
                tab3.error("❌ Invalid API Key. Please check your Gemini API key.")
            else:
                tab3.error(f"🚨 Unexpected Error: {e}")


# --- TAB 4: Contact ---
tab4.subheader("📬 Contact")
tab4.markdown("For more info, visit [Coinbase Index Page](https://www.coinbase.com/prime/indexes) 🔗")

# --- FOOTER ---
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ for Graduation Project | 2025 — From Code to Coin</p>", unsafe_allow_html=True)
