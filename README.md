# 📰 fake_news_detector

# Project Title: Fake News Detection App

# Description:

A web-based Fake News Detection application that uses Google Gemini API to analyze news text and determine whether it is Real or Fake, without relying on a pre-trained dataset or traditional ML models.

The Streamlit interface provides an easy-to-use and interactive web app where users can paste text, click a button, and instantly get a result indicating the authenticity of the news.

Fake news spreads rapidly and can mislead people. This project leverages the power of Large Language Models (LLMs) via the Gemini API to intelligently analyze news content and classify it as Fake or Real based on contextual understanding rather than static datasets.

Unlike conventional machine learning approaches, this system:

-Does not use a dataset
-Does not require model training
-Uses prompt-based inference through Gemini

# ✨ Features

🔍 Detects fake or real news using Gemini LLM

🧠 Context-aware text analysis

🌐 User-friendly web interface

⚡ Real-time predictions

🧩 No dataset or model training required

# 🛠️ Tech Stack

Python - Programming Language

Streamlit – Web interface

Google Gemini API – News analysis & classification

HTML / CSS – UI styling

IDE: VS Code

Libraries: scikit-learn, pandas, numpy, nltk, and Streamlit

# 🚀 How It Works

User enters a news article or headline

The text is sent to the Gemini API

Gemini analyzes credibility, tone, and content

The response is parsed and displayed as:

  ✅ Real News

  ❌ Fake News

# ⚠️ Limitations

Predictions depend on Gemini’s interpretation

Requires active internet connection

API usage is subject to rate limits and quota

Not a replacement for professional fact-checking
