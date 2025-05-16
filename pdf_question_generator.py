import nltk
from nltk.tokenize import sent_tokenize
from PyPDF2 import PdfReader
from transformers import pipeline

nltk.download("punkt")
nltk.download("punkt_tab")

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def chunk_text(text, max_tokens=300):
    sentences = sent_tokenize(text)
    chunks, current_chunk = [], []

    current_len = 0
    for sent in sentences:
        tokens = sent.split()
        if current_len + len(tokens) > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk, current_len = [], 0
        current_chunk.append(sent)
        current_len += len(tokens)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def generate_questions(chunks):
    question_model = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")
    results = []
    for chunk in chunks:
        prompt = f"generate question: {chunk}"
        result = question_model(prompt, max_length=64, do_sample=False)[0]["generated_text"]
        results.append((result, chunk))
    return results
