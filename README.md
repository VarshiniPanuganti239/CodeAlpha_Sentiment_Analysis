# 🤖 AI Sentiment Analysis Dashboard

An end-to-end Machine Learning web application that analyzes the sentiment of user-entered text and classifies it as **Positive**, **Negative**, or **Neutral**.

The project is built using **Python**, **Scikit-learn**, **TF-IDF Vectorization**, **Logistic Regression**, and **Streamlit**. It demonstrates the complete machine learning workflow, including data preprocessing, feature engineering, model training, evaluation, model serialization, and deployment through an interactive web application.

---

## 📌 Project Overview

Sentiment Analysis is a Natural Language Processing (NLP) task used to determine the emotional tone of text.

This project uses a Twitter Sentiment dataset to train a machine learning model capable of predicting the sentiment of unseen text.

The application provides:

- Real-time sentiment prediction
- Confidence score for predictions
- User-friendly Streamlit interface
- Interactive machine learning dashboard

---

## 🚀 Features

- Interactive Streamlit Web Application
- Text Cleaning and NLP Preprocessing
- TF-IDF Feature Extraction
- Logistic Regression Classifier
- Confidence Score Display
- Prediction for Custom User Input
- Clean and Professional User Interface
- Saved Model using Joblib
- Ready for Deployment

---

## 📂 Dataset

**Dataset:** Twitter Sentiment Analysis Dataset

Dataset contains tweets belonging to four classes:

- Positive
- Negative
- Neutral
- Irrelevant

Since **Irrelevant** tweets do not represent sentiment, they were removed before training to build a focused three-class sentiment classifier.

Training Dataset:
- `twitter_training.csv`

Validation Dataset:
- `twitter_validation.csv`

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib
- Streamlit
- Git & GitHub

---

## 🧠 Machine Learning Pipeline

### 1. Data Loading

- Loaded training dataset
- Loaded validation dataset

### 2. Data Cleaning

- Removed missing values
- Removed duplicate records
- Removed "Irrelevant" class
- Reset dataframe index

### 3. Text Preprocessing

Performed NLP preprocessing including:

- Lowercase conversion
- Removal of URLs
- Removal of punctuation
- Removal of numbers
- Tokenization
- Stopword removal
- Lemmatization

### 4. Feature Engineering

Used **TF-IDF Vectorizer** with:

- Maximum Features = 5000

### 5. Label Encoding

Encoded sentiment labels into numerical format.

### 6. Model Training

Algorithm Used:

- Logistic Regression

### 7. Model Evaluation

Evaluated using the validation dataset.

Performance metrics include:

- Accuracy Score
- Classification Report
- Confusion Matrix

### 8. Model Serialization

Saved the trained components using Joblib:

- sentiment_model.pkl
- tfidf_vectorizer.pkl
- label_encoder.pkl

### 9. Web Application

Built using Streamlit.

Features include:

- User text input
- Sentiment prediction
- Confidence score
- Clean dashboard interface

---

## 📁 Project Structure

```
CodeAlpha_Sentiment_Analysis/
│
├── app.py
├── utils.py
├── Sentiment_Analysis.ipynb
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
├── twitter_training.csv
├── twitter_validation.csv
│
└── screenshots/
    ├── home_page.png
    ├── positive_prediction.png
    ├── negative_prediction.png
    └── neutral_prediction.png
```

---

## 📊 Model Information

| Parameter | Value |
|-----------|-------|
| Algorithm | Logistic Regression |
| Feature Extraction | TF-IDF |
| Dataset | Twitter Sentiment Dataset |
| Classes | Positive, Negative, Neutral |
| NLP | TF-IDF + Text Cleaning |
| Deployment | Streamlit |

---

## 🖥️ Screenshots

### 🏠 Home Page

![Home Page](screenshots/home_page.png)

---

### 😊 Positive Prediction

![Positive Prediction](screenshots/positive_prediction.png)

---

### 😐 Neutral Prediction

![Neutral Prediction](screenshots/neutral_prediction.png)

---

### 😞 Negative Prediction

![Negative Prediction](screenshots/negative_prediction.png)

---

⚙️ Installation

Clone Repository

```bash
git clone https://github.com/VarshiniPanuganti239/CodeAlpha_Sentiment_Analysis.git
```

Go to project folder

```bash
cd CodeAlpha_Sentiment_Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

💡 Example Predictions

| Input | Prediction |
|--------|------------|
| I absolutely love this product. | Positive 😊 |
| This is the worst experience ever. | Negative 😞 |
| The meeting starts at 10 AM tomorrow. | Neutral 😐 |

---

🔮 Future Improvements

- Deep Learning based sentiment classifier
- BERT/RoBERTa transformer model
- Emotion Detection
- Multi-language sentiment analysis
- Explainable AI (SHAP/LIME)
- Deployment on Streamlit Cloud
- REST API using FastAPI

---

📈 Learning Outcomes

Through this project I learned:

- Data preprocessing
- Natural Language Processing
- TF-IDF Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- Model Serialization
- Streamlit Deployment
- Git & GitHub Project Management

---

👩‍💻 Developed By

Panuganti Varshini

Machine Learning & Artificial Intelligence Enthusiast

GitHub:
https://github.com/VarshiniPanuganti239

📄 License

This project is developed for educational and internship purposes under the **CodeAlpha Artificial Intelligence Internship**.
