# 💬 Sentiment Analysis Web App

This is a simple yet powerful **Streamlit app** that performs **sentiment analysis** using a **pretrained RoBERTa model** (`cardiffnlp/twitter-roberta-base-sentiment`) from 🤗 Hugging Face Transformers.

It classifies text into **Positive**, **Neutral**, or **Negative** sentiments — perfect for analyzing tweets, reviews, or any user feedback.

---

## 🚀 Live Demo


---

## 🧠 Model Info

- **Model**: [`cardiffnlp/twitter-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)
- **Classes**: `LABEL_0` = Negative, `LABEL_1` = Neutral, `LABEL_2` = Positive
- **Trained on**: Millions of English tweets

---

## 📦 Requirements

Make sure to install the following:

```bash
pip install streamlit transformers torch

