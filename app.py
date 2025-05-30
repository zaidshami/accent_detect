import streamlit as st
from agent import process_video_url
from streamlit_lottie import st_lottie
import json
import os
import streamlit as st

openai_key = st.secrets["api_keys"]["openai"]

os.environ["OPENAI_API_KEY"] = openai_key

# Loadv animations
def load_lottie(path):
    with open(path, "r") as f:
        return json.load(f)

lottie_loading = load_lottie("assets/new_load.json")
lottie_success = load_lottie("assets/success.json")

# Page config
st.set_page_config(page_title="Accent Classifier", page_icon="🎧", layout="centered")
st.markdown('<style>' + open('style/custom.css').read() + '</style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🎙️ English Accent Evaluator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Evaluate spoken English from video links. Perfect for smart hiring!</p>", unsafe_allow_html=True)

video_url = st.text_input("🔗 Paste a video,audio URL ")

if st.button("🚀 Analyze Video"):
    if not video_url:
        st.warning("Please enter a valid video URL.")
    else:
        st_lottie(lottie_loading, height=200, key="loading")
        with st.spinner("Extracting, transcribing, analyzing..."):
            results = process_video_url(video_url)

        st.balloons()
        st_lottie(lottie_success, height=200, key="success")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="🧭 Accent", value=results["accent"])
        with col2:
            st.metric(label="💬 English Fluency Score", value=f'{results["confidence"]}%')

        st.markdown("### 💡 Explanation")
        st.info(results["explanation"])