# 📘 PDF Question Generator

A Python-based tool that extracts text from PDF documents and generates questions using a pretrained NLP model. Ideal for educators, trainers, and anyone looking to automate the process of question generation from textual content.

## 🚀 Features

- 📄 Extracts text from PDFs
- 🤖 Generates questions using a pretrained T5 model (`google/flan-t5-base`)
- 🧠 Categorizes questions into difficulty levels *(coming soon)*
- ✅ Multiple Choice Question (MCQ) support *(coming soon)*
- 🖼️ Simple Gradio UI for ease of use

## 🧰 Tech Stack

- Python 3.8+
- [Transformers (Hugging Face)](https://huggingface.co/transformers/)
- [nltk](https://www.nltk.org/)
- [Gradio](https://gradio.app/)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/pdf-question-generator.git
   cd pdf-question-generator

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK tokenizer data**:

   ```python
   import nltk
   nltk.download('punkt')
   ```


## 📁 Project Structure

```text
pdf-question-generator/
├── main.py                 # Entry point to launch the Gradio UI
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── sample_pdfs/            # Folder to store example PDF files
