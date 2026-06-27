# ============================================================
# AI Sentiment Analysis Dashboard
# Author: Panuganti Varshini
# ============================================================

import streamlit as st
import pandas as pd
from datetime import datetime

from utils import predict_sentiment, get_probability_scores

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI Sentiment Analysis Dashboard",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# Session State
# ============================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ============================================================
# Custom CSS
# ============================================================

st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#00D4FF;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:18px;
    border-radius:10px;
}

.result-box{
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    border:2px solid #00D4FF;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("🤖 AI Dashboard")

st.sidebar.markdown("---")

st.sidebar.write("### Model Information")

st.sidebar.write("Algorithm : Logistic Regression")

st.sidebar.write("Feature Extraction : TF-IDF")

st.sidebar.write("Dataset : Twitter Sentiment Dataset")

st.sidebar.write("Classes : Positive, Neutral, Negative")

st.sidebar.markdown("---")

st.sidebar.write("### Developed By")

st.sidebar.write("Panuganti Varshini")

# ============================================================
# Title
# ============================================================

st.markdown(
    '<p class="main-title">AI Sentiment Analysis Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning | NLP | Streamlit</p>',
    unsafe_allow_html=True
)

st.markdown("---")
# ============================================================
# User Input
# ============================================================

st.header("📝 Enter Text")

user_text = st.text_area(
    "Type your text below:",
    height=180,
    placeholder="Example: I really enjoyed this new AI project!"
)

predict_button = st.button("🚀 Analyze Sentiment")

# ============================================================
# Prediction
# ============================================================

if predict_button:

    if user_text.strip() == "":
        st.warning("⚠ Please enter some text.")
    else:

        sentiment, confidence, probabilities = predict_sentiment(user_text)

        st.markdown("## Prediction Result")

        if sentiment.lower() == "positive":
            st.success(f"😊 Sentiment: {sentiment}")

        elif sentiment.lower() == "negative":
            st.error(f"😞 Sentiment: {sentiment}")

        else:
            st.info(f"😐 Sentiment: {sentiment}")

        st.metric(
            label="Confidence Score",
            value=f"{confidence:.2f}%"
        )

        # Save history
        st.session_state.history.append({
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Text": user_text,
            "Sentiment": sentiment,
            "Confidence": round(confidence, 2)
        })

        st.markdown("---")