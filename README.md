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

# 🎯 Project Objective 

Objective:

The objective of this project is to develop a Fake News Detection system that analyzes the linguistic and stylistic patterns of news text using a pre-trained transformer-based language model. The system aims to classify news articles as Likely Real or Likely Fake based on learned textual features, rather than factual verification.

This project focuses on:

Understanding how Natural Language Processing (NLP) models analyze news content

Implementing an end-to-end AI-powered web application using Streamlit

Demonstrating the strengths and limitations of machine learning–based fake news classification

The system is intended as a decision-support tool and not as a definitive fact-checking solution.

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

While the Fake News Detector provides useful insights, it has several limitations:

No Fact Verification
The system does not verify whether an event actually occurred. It evaluates only the writing style and language patterns of the input text.

No Access to Real-World Databases
The model does not cross-check information against news archives, government records, or fact-checking databases.

Domain Dependency
The model is trained primarily on political and social news articles. As a result:

Scientific facts

Health-related statements

General knowledge content
may be misclassified.

Well-Written Fake News May Appear Real
Fake news written in a formal journalistic style may be classified as Likely Real, leading to false negatives.

Out-of-Distribution Inputs
Short statements, opinions, or non-news content may produce unreliable predictions due to mismatch with training data.

Confidence Scores Are Not Guarantees
High confidence values reflect model certainty, not factual correctness.

# ✅ Conclusion

Successfully built a Fake News Detection Web App

Implemented using:

   VS Code
   Streamlit
   Gemini API

No dataset or model training required
Real-time, AI-powered predictions
