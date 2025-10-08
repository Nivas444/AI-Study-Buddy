import streamlit as st
from modules.ocr_module import pdf_to_text, image_to_text
from modules.youtube_module import summarize_youtube
from modules.summarizer import summarize_text
from modules.quiz_module import generate_mcqs
from modules.voice_module import speak_text, speech_to_text
from modules.semantic_search import semantic_search
from modules.gamification import init_db, update_xp

st.title("🎓 AI Study Buddy")

init_db()  # Initialize gamification DB

menu = ["Upload Notes", "YouTube Summarizer", "Quiz Mode", "Voice Interaction"]
choice = st.sidebar.selectbox("Select Feature", menu)

if choice == "Upload Notes":
    uploaded_file = st.file_uploader("Upload PDF/Image", type=["pdf", "jpg", "png"])
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            text = pdf_to_text(uploaded_file)
        else:
            text = image_to_text(uploaded_file)
        st.text_area("Extracted Text", text)

elif choice == "YouTube Summarizer":
    video_id = st.text_input("Enter YouTube Video ID")
    if st.button("Summarize"):
        summary = summarize_youtube(video_id)
        st.text_area("Summary", summary)

elif choice == "Quiz Mode":
    text = st.text_area("Enter Notes Text")
    if st.button("Generate MCQs"):
        mcqs = generate_mcqs(text)
        for q in mcqs:
            st.write(f"Q: {q['question']}")
            st.write(f"A: {q['answer']}")
        update_xp("user1", 10)

elif choice == "Voice Interaction":
    st.write("Ask your question (via uploaded audio)")
    audio_file = st.file_uploader("Upload audio", type=["wav", "mp3"])
    if audio_file:
        query = speech_to_text(audio_file)
        st.write("You asked:", query)
        response = "This is a demo response from AI."
        speak_text(response)
        st.write("AI says:", response)
