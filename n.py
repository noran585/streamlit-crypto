import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import google.generativeai as genai

# -------- PAGE CONFIG --------
st.set_page_config(page_title="COIN50 Index", layout="wide")

# -------- THEME SWITCH --------
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

# -------- HEADER TITLE --------
st.markdown("""
    <h1 style='text-align: center;'>From Code to Coin 💻🪙🔗</h1>
""", unsafe_allow_html=True)

# -------- TABS --------
tab1, tab2, tab3 = st.tabs(["Prediction and Insights", "COIN50 Constituents", "Generative AI"])

# -------- TAB 1: PREDICTION AND INSIGHTS --------
with tab1:
    st.markdown("### 🧠 Introduction")
    st.markdown("""
        The COIN50 Index is a comprehensive benchmark that tracks the top 50 cryptocurrencies listed on Coinbase,
        providing a diversified and dynamic view of the digital asset market. It uses a transparent methodology that
        incorporates market capitalization and liquidity as core criteria while applying caps and filters to reduce
        volatility and concentration risk. The index is rebalanced quarterly to reflect market changes, helping analysts,
        traders, and investors to understand broader crypto trends and performance with clarity.
    """)

    st.subheader("📈 Coinbase 50 Index Trend (Mock Data)")
    dates = pd.date_range(start='2023-01-01', periods=100)
    index_values = np.cumsum(np.random.normal(loc=0.1, scale=1.0, size=100)) + 100
    df_trend = pd.DataFrame({"Date": dates, "Coinbase50_Index": index_values})
    fig = px.line(df_trend, x="Date", y="Coinbase50_Index", title="Coinbase 50 Index Trend", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 🔍 For more information")
    st.markdown("🔗 [Visit the Coinbase Index Page](https://www.coinbase.com/prime/indexes)")

# -------- TAB 2: COIN50 Constituents (Bar Chart + Table) --------
with tab2:
    st.subheader("📊 Full COIN50 Components & Weights")

    coin_data = {
        "Component": [
            "Bitcoin", "Ethereum", "XRP", "Solana", "Dogecoin", "Cardano", "Bitcoin Cash", "Chainlink",
            "Stellar Lumen", "Avalanche", "Shiba Inu", "Litecoin", "Polkadot", "Uniswap Protocol Token", "Pepe (pepe.vip)",
            "Aave", "Aptos", "Internet Computer", "Near", "Ethereum Classic", "Polygon Ecosystem Token",
            "Artificial Superintelligence Alliance", "Maker", "Render Network", "Cosmos", "Quant", "Algorand", "BONK",
            "Celestia", "Injective", "Stacks", "Convex Finance", "The Graph", "Curve DAO Token", "Aerodrome Finance",
            "Lido DAO", "The Sandbox", "JasmyCoin", "Tezos", "Decentraland", "ApeCoin", "Compound", "Helium",
            "Axie Infinity Shards", "Chiliz", "Akash Network", "1inch", "Livepeer", "Synthetix", "Oasis"
        ],
        "Weight": [
            51.14, 22.73, 9.46, 5.68, 1.88, 1.58, 0.69, 0.63, 0.58, 0.58, 0.51, 0.48, 0.43, 0.35, 0.32, 0.30, 0.21,
            0.20, 0.19, 0.19, 0.13, 0.13, 0.13, 0.12, 0.12, 0.11, 0.11, 0.08, 0.08, 0.08, 0.07, 0.06, 0.06, 0.06,
            0.05, 0.05, 0.05, 0.05, 0.04, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0.01
        ]
    }

    df_constituents = pd.DataFrame(coin_data)

    # Bar Chart (Top 10 Only) with neutral color
    top10 = df_constituents.sort_values(by="Weight", ascending=False).head(10)
    fig_weights = px.bar(
        top10,
        x="Component",
        y="Weight",
        title="Top 10 COIN50 Weights",
        labels={"Component": "Cryptocurrency", "Weight": "Weight (%)"},
    )
    fig_weights.update_traces(marker_color='blue')  # neutral color
    fig_weights.update_layout(yaxis=dict(title="Weight (%)"), xaxis=dict(title=""))

    st.plotly_chart(fig_weights, use_container_width=True)

    # Full Table
    st.markdown("### 📋 Full COIN50 Table")
    st.dataframe(df_constituents, use_container_width=True)


# -------- TAB 3: GENERATIVE AI --------
with tab3:
    st.subheader("🤖 Generative AI-Powered Crypto Assistant")

    API_KEY = "AIzaSyA2R5r3D0CkyWQd3nf3FKkAVeDAFswJzEM"  # Replace with your actual API key
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = st.text_input("Ask anything about crypto (e.g., Bitcoin, Ethereum, blockchain):")
    if prompt:
        with st.spinner("Thinking with Gemini..."):
            try:
                response = model.generate_content(prompt)
                st.success("🤖 " + response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# -------- FOOTER --------
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ for Graduation Project | 2025 — From Code to Coin</p>", unsafe_allow_html=True)
