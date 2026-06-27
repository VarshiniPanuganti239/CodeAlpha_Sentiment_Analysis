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

<img width="950" height="526" alt="Home Page" src="https://github.com/user-attachments/assets/65412d6f-33b9-47ba-a36e-39d0778adae4" />

---

### 😊 Positive Prediction

<img width="955" height="535" alt="Positive Prediction" src="https://github.com/user-attachments/assets/1b3f2b7b-03b4-4e4c-a83d-ff6f118d395f" />


---

### 😐 Neutral Prediction

<img width="955" height="528" alt="Neutral Prediction" src="https://github.com/user-attachments/assets/bb68c25e-ef8c-41ab-8cac-5ecff6863269" />

---

### 😞 Negative Prediction

<img width="951" height="560" alt="Negative Prediction" src="https://github.com/user-attachments/assets/dfc68690-7a6d-4cb2-bbf3-05062f6c0f3f" />

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
