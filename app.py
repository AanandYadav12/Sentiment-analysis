import streamlit as st
from transformers import pipeline

# Load the model and tokenizer
classifier = pipeline("sentiment-analysis",
                      model="cardiffnlp/twitter-roberta-base-sentiment",
                      tokenizer="cardiffnlp/twitter-roberta-base-sentiment")

# Streamlit app layout
st.title("💬 Sentiment Analysis App")
st.write("Enter text to see if it's Positive, Neutral, or Negative.")

text = st.text_area("Enter your text here:", "It's amazing!")

if st.button("Analyze Sentiment"):
    result = classifier(text)[0]

    # Optional label mapping (can be skipped)
    label_map = {
        'LABEL_0': 'Negative',
        'LABEL_1': 'Neutral',
        'LABEL_2': 'Positive'
    }

    label = label_map.get(result['label'], result['label'])
    score = round(result['score'] * 100, 2)

    st.markdown(f"**Sentiment:** {label} ({score}%)")
