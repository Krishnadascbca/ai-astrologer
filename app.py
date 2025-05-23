import streamlit as st
from prompts import generate_insight

st.set_page_config(page_title="🔮 AI Astrologer", layout="centered")
st.title("🔮 AI Astrologer")
st.markdown("Welcome! Ask a question and receive astrological insights ✨")

name = st.text_input("Enter your name:")
birthdate = st.date_input("Select your birthdate:")
birthtime = st.time_input("Enter your birth time (optional):")
zodiac = st.selectbox("Choose your zodiac sign (optional):", [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Prefer not to say"
])
question = st.text_area("What would you like to ask the astrologer?")

if st.button("Get Insight"):
    insight = generate_insight(name, birthdate, birthtime, zodiac, question)
    st.markdown("### 🌟 Your Astrological Insight")
    st.write(insight)
