import streamlit as st
from transformers import pipeline

# --- 1. Load Custom CSS for Styling ---
def local_css(file_name):
    """Function to load a local CSS file."""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- 2. Page Configuration and Introduction ---
st.set_page_config(page_title="Fake News Detector", layout="wide")

# Apply the custom CSS
local_css("style.css")

# Use a newspaper emoji 📰 or an icon class if using a library that supports it
st.title("📰 Fake News Detector")
st.write("Enter a news headline or a short article. This demo uses a pre-trained language model to assess the likelihood of fake news.")
st.write("---")

# --- 3. Load the NLP Model (Cached) ---
@st.cache_resource
def load_model():
    """Loads and returns the pre-trained text classification model."""
    return pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")

nlp_pipeline = load_model()

# --- 4. User Input Section ---
user_input = st.text_area(
    "Paste news headline or story below:",
    height=200,
    placeholder="Example: Due to rain, Monday is declared a holiday."
)

# --- 5. Prediction Logic ---
if st.button("Check News", type="primary") and user_input.strip():
    with st.spinner("Analyzing..."):
        # Get raw prediction from the model
        result = nlp_pipeline(user_input)
        
        raw_label = result[0]['label']
        score = result[0]['score']

        # Map the model's internal labels to human-readable ones
        label_map = {
            "LABEL_1": "FAKE",
            "LABEL_0": "REAL"
        }
        display_label = label_map.get(raw_label, "Unknown")

        st.write("---")
        st.subheader("Prediction Result")
        
        # Display results in styled metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Prediction", display_label)
        with col2:
            st.metric("Confidence", f"{score:.2%}")
            
        # Provide feedback based on the result
        if display_label == "FAKE":
            st.warning("This text shows characteristics of **fake news**. Please verify the information from trusted sources before sharing.")
        elif display_label == "REAL":
            st.success("This text appears to be **real news** based on the model's analysis.")

# --- 6. Footer ---
st.write("---")
st.markdown("<div style='text-align: center; color: #A3A3A3;'><em>This tool provides a prediction based on a trained AI model and is not a guarantee of truth. Always use critical judgment.</em></div>", unsafe_allow_html=True)
