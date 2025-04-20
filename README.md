📩 Ham or Spam?

An intelligent SMS Spam Classifier that not only detects whether a message is ham or spam, but also explains why — powered by Groq's LLM API.

🚀 Demo

Live Streamlit App 👉 Click Here to Try (replace with your real app URL)

🔍 Features

✅ Classifies SMS messages as spam or ham

🔍 Uses Logistic Regression with TF-IDF vectorization

🤖 Integrates Groq API to provide natural language explanations

📊 High recall and precision (especially on spam detection)

🔐 Secure deployment via Streamlit Secrets

🧠 Tech Stack

Python 3.x

Streamlit

Scikit-learn

Pandas

Groq LLM API

📂 Project Structure

ham-or-spam/
├── app.py                  # Streamlit app
├── sms_pipeline.pkl        # Trained ML model with TF-IDF
├── requirements.txt        # Dependencies
└── README.md               # Project overview

🧪 How to Run Locally

Clone this repo:

git clone https://github.com/yourusername/ham-or-spam.git
cd ham-or-spam

Install dependencies:

pip install -r requirements.txt

Set your Groq API key:

export GROQ_API_KEY=your_groq_key_here

Run the app:

streamlit run app.py

🌐 Deployment on Streamlit Cloud

Push code to GitHub

Go to Streamlit Cloud → New App

Choose your repo and app.py

Add a secret:

Key: GROQ_API_KEY

Value: your actual Groq API key

Click Deploy 🚀

📊 Model Performance

Classifier: Logistic Regression (balanced)

Spam Recall: 0.94

Spam Precision: 0.90

🤖 Powered by Groq

The app uses Groq API to generate natural language explanations for each SMS classification.
