import streamlit as st
import pandas as pd
import pickle
import requests
from sklearn.pipeline import Pipeline

# ---- Load your trained pipeline (tfidf + classifier) ----
@st.cache_resource
def load_model():
    with open("sms_pipeline.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# ---- Groq API Config ----
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# ---- Function to get explanation from Groq API ----
def get_explanation(message, prediction_label):
    prompt = (
        f"The following SMS message was classified as '{prediction_label}'. "
        f"Here is the message: \n" + message + "\n"
        "Explain why this message might be considered as '" + prediction_label + "'."
    )
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(GROQ_API_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "❌ Could not generate explanation."

# ---- Streamlit App UI ----
st.title("📩 SMS Spam Classifier with Explanation")
st.markdown("Classify an SMS as Spam or Ham and understand why.")

message = st.text_area("Enter your SMS message:", "")

if st.button("Analyze Message"):
    if not message.strip():
        st.warning("⚠️ Please enter a message first.")
    else:
        pred = model.predict([message])[0]
        label = "spam" if pred == 1 else "ham"
        proba = model.predict_proba([message])[0][pred]

        st.subheader(f"Prediction: {'🚨 SPAM' if label == 'spam' else '✅ HAM'}")
        # st.write(f"Confidence: **{proba:.2f}**")

        with st.spinner("Generating explanation using Groq API..."):
            explanation = get_explanation(message, label)
        st.markdown("---")
        st.subheader("🤖 Why this prediction?")
        st.write(explanation)
