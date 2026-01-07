import streamlit as st
from transformers import pipeline

# ---------- Page Config ----------
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

# ---------- Load Custom CSS ----------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ---------- Header Section ----------
st.markdown(
    """
    <div style="text-align:center; padding: 10px 0;">
        <h1>📰 Fake News Detector</h1>
        <p style="font-size:18px; color:#b0b0b0;">
            Analyze news headlines or short articles using AI
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- Model Loading ----------
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="mrm8488/bert-tiny-finetuned-fake-news-detection",
        framework="pt"
    )

nlp_pipeline = load_model()

# ---------- Input Section ----------
st.subheader("📥 Enter News Text")

user_input = st.text_area(
    label="",
    height=180,
    placeholder="Example:\nDue to heavy rainfall, Monday is declared a public holiday across the state."
)

st.write("")  # spacing

# ---------- Action Button ----------
analyze_btn = st.button("🔍 Analyze News", use_container_width=True)

# ---------- Prediction Section ----------
if analyze_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter some news text before analyzing.")
    else:
        with st.spinner("🧠 Analyzing the content..."):
            result = nlp_pipeline(user_input)

            raw_label = result[0]["label"]
            score = result[0]["score"]

            label_map = {
                "LABEL_1": "FAKE",
                "LABEL_0": "REAL"
            }
            prediction = label_map.get(raw_label, "Unknown")

        st.divider()
        st.subheader("📊 Prediction Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="🧾 Classification",
                value=prediction
            )

        with col2:
            st.metric(
                label="📈 Confidence",
                value=f"{score:.2%}"
            )

        # ---------- Feedback Message ----------
        if prediction == "FAKE":
            st.error(
                "🚨 **This news is likely FAKE.**\n\n"
                "The content shows patterns commonly found in misinformation. "
                "Please verify from trusted news sources."
            )
        elif prediction == "REAL":
            st.success(
                "✅ **This news appears to be REAL.**\n\n"
                "The content aligns with credible language patterns. "
                "However, always cross-check important information."
            )

# ---------- Footer ----------
st.divider()
st.markdown(
    """
    <div style="text-align:center; font-size:14px; color:#9a9a9a;">
        <em>
        This tool provides AI-based predictions and does not guarantee factual accuracy.<br>
        Always apply critical thinking and verify from reliable sources.
        </em>
    </div>
    """,
    unsafe_allow_html=True
)
