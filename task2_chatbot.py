import streamlit as st
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Pre-defined Knowledge Base (FAQs)
FAQS = [
    {"q": "What is CodeAlpha internship?", "a": "CodeAlpha provides virtual internships across various tech domains with real-world project exposure."},
    {"q": "How many tasks do I need to complete?", "a": "You need to complete at least 2 or 3 tasks to qualify for the completion certificate."},
    {"q": "How do I submit my project?", "a": "Upload your code to GitHub named CodeAlpha_ProjectName, share a LinkedIn video demo, and submit via the Google Form."},
    {"q": "When will I get my internship completion certificate?", "a": "Certificates with unique verification IDs are issued after review of your task submissions."},
    {"q": "Is the internship free?", "a": "Yes, completing tasks and earning certificates follows CodeAlpha's free open-learning program guidelines."},
    {"q": "How can I contact support?", "a": "You can email services@codealpha.tech or reach out on WhatsApp support."}
]

# Step 2: Vectorizer & Preprocessing setup
questions = [faq["q"] for faq in FAQS]
vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
tfidf_matrix = vectorizer.fit_transform(questions)

def get_best_answer(user_query: str, threshold: float = 0.25):
    query_vec = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]
    
    if best_score < threshold:
        return "I'm sorry, I don't have enough information on that. Please contact support via services@codealpha.tech."
    return FAQS[best_idx]["a"]

# Step 3: Streamlit UI
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")
st.title("🤖 Customer Support FAQ Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Ask me any question about the internship program."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    bot_reply = get_best_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)