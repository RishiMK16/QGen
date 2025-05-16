import streamlit as st
from pdf_question_generator import extract_text_from_pdf, chunk_text, generate_questions
import os

st.set_page_config(page_title="📘 PDF Question Generator", layout="centered")

st.title("📘 PDF Question Generator")
st.write("Upload a PDF and get questions generated using a T5 model.")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    file_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("🔍 Extracting text from PDF..."):
        text = extract_text_from_pdf(file_path)

    if not text.strip():
        st.error("No readable text found in the PDF.")
    else:
        with st.spinner("✂️ Chunking text..."):
            chunks = chunk_text(text)

        with st.spinner("🤖 Generating questions..."):
            qa_pairs = generate_questions(chunks[:5])  # limit to 5 chunks for speed

        st.success("✅ Questions Generated!")

        for i, (question, context) in enumerate(qa_pairs, start=1):
            st.markdown(f"### ❓ Question {i}")
            st.write(question)
            with st.expander("📄 Show Context"):
                st.write(context)
