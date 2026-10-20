import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Language Translator", layout="centered")

st.title("🌐 Real-time Language Translator")
st.write("Free multi-language translation powered by Deep-Translator.")

# Language dictionary mapping display names to ISO codes
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Gujarati": "gu",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Arabic": "ar",
    "Russian": "ru"
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", ["Auto Detect"] + list(LANGUAGES.keys()))
with col2:
    target_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=0)

input_text = st.text_area("Enter text to translate:", height=150, placeholder="Type your text here...")

if st.button("Translate", type="primary"):
    if not input_text.strip():
        st.warning("Please enter some text first.")
    else:
        src = "auto" if source_lang == "Auto Detect" else LANGUAGES[source_lang]
        tgt = LANGUAGES[target_lang]
        try:
            translated = GoogleTranslator(source=src, target=tgt).translate(input_text)
            st.success("Translation Complete:")
            st.text_area("Result:", value=translated, height=150)
            
            # Usability feature: Quick copy tip / raw markdown display
            st.code(translated, language=None)
        except Exception as e:
            st.error(f"Error during translation: {e}")