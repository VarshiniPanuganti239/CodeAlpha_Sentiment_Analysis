# ============================================================
# AI Sentiment Analysis System
# Utility Functions
# Author: Panuganti Varshini
# ============================================================

import re
import joblib
import numpy as np

# ============================================================
# Load Saved Model Files
# ============================================================

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")


# ============================================================
# Text Preprocessing Function
# ============================================================

def clean_text(text):
    """
    Clean and preprocess the input text.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove user mentions
    text = re.sub(r"@\w+", "", text)

    # Remove hashtag symbol but keep the word
    text = re.sub(r"#", "", text)

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ============================================================
# Sentiment Prediction Function
# ============================================================

def predict_sentiment(text):
    """
    Predict sentiment for a given text.
    Returns:
        sentiment (str)
        confidence (float)
        probabilities (numpy array)
    """

    # Clean the text
    cleaned_text = clean_text(text)

    # Convert text to TF-IDF features
    text_vector = vectorizer.transform([cleaned_text])

    # Predict sentiment
    prediction = model.predict(text_vector)[0]

    # Prediction probabilities
    probabilities = model.predict_proba(text_vector)[0]

    # Highest probability
    confidence = np.max(probabilities) * 100

    # Convert label back to text
    sentiment = label_encoder.inverse_transform([prediction])[0]

    return sentiment, confidence, probabilities


# ============================================================
# Probability Dictionary
# ============================================================

def get_probability_scores(probabilities):
    """
    Returns probability scores for each sentiment class.
    """

    class_names = label_encoder.classes_

    scores = {}

    for i in range(len(class_names)):
        scores[class_names[i]] = round(probabilities[i] * 100, 2)

    return scores