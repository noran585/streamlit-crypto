import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import requests
import time
import random

# Configure page
st.set_page_config(page_title="COIN50 Index", layout="wide")

# --- Theme Switch with Icons ---
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

# Title
st.markdown("""
    <h1 style='text-align: center;'>From Code to Coin 💻🪙🔗</h1>
    <p style='text-align: center; color: grey;'>Your Gateway to Understanding the Coinbase 50 Index</p>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Charts", "Chatbot", "Prediction and Insights", "Contact"])

# Coin data
coins = [
    {"name": "Bitcoin", "weight": 50.30, "logo": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png", "id": "bitcoin"},
    {"name": "Ethereum", "weight": 22.69, "logo": "https://assets.coingecko.com/coins/images/279/large/ethereum.png", "id": "ethereum"},
    {"name": "XRP", "weight": 9.37, "logo": "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png", "id": "ripple"},
    {"name": "Solana", "weight": 5.91, "logo": "https://assets.coingecko.com/coins/images/4128/large/solana.png", "id": "solana"},
    {"name": "Dogecoin", "weight": 2.12, "logo": "https://assets.coingecko.com/coins/images/5/large/dogecoin.png", "id": "dogecoin"},
    {"name": "Cardano", "weight": 1.76, "logo": "https://assets.coingecko.com/coins/images/975/large/cardano.png", "id": "cardano"},
    {"name": "Chainlink", "weight": 0.67, "logo": "https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png", "id": "chainlink"},
    {"name": "Avalanche", "weight": 0.64, "logo": "https://assets.coingecko.com/coins/images/12559/large/coin-round-red.png", "id": "avalanche-2"},
    {"name": "Stellar Lumen", "weight": 0.61, "logo": "https://assets.coingecko.com/coins/images/100/large/Stellar_symbol_black_RGB.png", "id": "stellar"},
    {"name": "Bitcoin Cash", "weight": 0.59, "logo": "https://assets.coingecko.com/coins/images/780/large/bitcoin-cash-circle.png", "id": "bitcoin-cash"},
]
df = pd.DataFrame(coins)

# OVERVIEW TAB
tab1.subheader("🪙 COIN50 Index Components (Top 10)")
cols = tab1.columns(5)
for i, coin in enumerate(coins):
    with cols[i % 5]:
        st.image(coin["logo"], width=60)
        st.markdown(f"{coin['name']}", unsafe_allow_html=True)
        st.markdown(f"<span style='color: green;'>Weight: {coin['weight']}%</span>", unsafe_allow_html=True)

tab1.markdown("### 📘 Index Methodology")
tab1.markdown("""
The COIN50 index is designed to track the performance of the top 50 cryptocurrencies listed on Coinbase. 
It uses market capitalization and liquidity as the primary selection criteria, and is periodically rebalanced to reflect the dynamic nature of the crypto market. 
The goal is to provide a clear and comprehensive view of the broader digital asset landscape for investors and analysts alike.
Additional considerations include filtering out illiquid or highly volatile assets and applying a cap on maximum allocation to ensure diversification.
The index is reviewed quarterly and methodology updates are publicly disclosed to maintain transparency.

Weights are assigned proportionally to each coin’s market cap within the eligible pool. A liquidity screen ensures assets can be traded efficiently. The index aims to capture broad market movement while reducing overexposure to single assets.

Each rebalance includes risk assessment metrics and is performed using transparent, auditable procedures.
""")

# CHARTS TAB
tab2.subheader("📊 Market Cap Distribution (Mock Data)")
coin_names = [coin["name"] for coin in coins]
weights = [coin["weight"] for coin in coins]
fig_bar = px.bar(x=coin_names, y=weights, labels={"x": "Coin", "y": "Weight (%)"}, title="Coin Weights in Index")
tab2.plotly_chart(fig_bar, use_container_width=True)

tab2.markdown("### 💡 Fun Fact")
fact = random.choice([
    "The first real-world Bitcoin transaction was for two pizzas.",
    "Over 20% of all Bitcoin is estimated to be lost forever due to lost private keys.",
])
tab2.info(fact)

# CHATBOT + QUIZ TAB
tab3.subheader("🤖 Ask the Crypto Bot (Powered by Wikipedia)")
def search_wiki(query):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get("extract", "No result found.")
    else:
        return "Sorry, I couldn't find anything."

question = tab3.text_input("Ask anything about crypto (e.g., Bitcoin, Ethereum, blockchain):")
if question:
    with st.spinner("Searching Wikipedia..."):
        answer = search_wiki(question)
        tab3.success("🤖 " + answer)

# Quiz inside tab3
tab3.markdown("---")
tab3.subheader("🧠 Quick Crypto Quiz")

quiz_question = "What is the total supply of Bitcoin?"
quiz_options = ["21 Million", "100 Million", "Unlimited", "50 Million"]
selected = tab3.radio("What is the total supply of Bitcoin?:", quiz_options, key="quiz")

if tab3.button("Submit Quiz Answer"):
    if selected == "21 Million":
        tab3.success("✅ Correct! Bitcoin has a fixed supply of 21 Million coins.")
    else:
        tab3.error("❌ Incorrect. The correct answer is 21 Million.")

# PREDICTION TAB
tab4.subheader("📈 Prediction and Insights")
dates = pd.date_range(start='2023-01-01', periods=100)
index_values = np.cumsum(np.random.normal(loc=0.1, scale=1.0, size=100)) + 100
df_trend = pd.DataFrame({"Date": dates, "Coinbase50_Index": index_values})
fig = px.line(df_trend, x="Date", y="Coinbase50_Index", title="Coinbase 50 Index Trend", markers=True)
tab4.plotly_chart(fig, use_container_width=True)

# CONTACT TAB
tab5.subheader("📬 Contact")
tab5.markdown("For more info, visit [Coinbase Index Page](https://www.coinbase.com/prime/indexes) 🔗")

# FOOTER
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ for Graduation Project | 2025 — From Code to Coin</p>", unsafe_allow_html=True)
