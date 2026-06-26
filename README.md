# 📚 AI Book Chat Assistant

A simple Retrieval-Augmented Generation (RAG) application that lets you upload a PDF and ask questions about its content.

## Features

* Upload any PDF document
* Chat with the uploaded PDF
* Retrieves relevant information before generating answers
* Simple and interactive Streamlit interface

## Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Mistral AI

## Project Structure

```text
RAG-PDF-Chatbot/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/RAG-PDF-Chatbot.git
cd RAG-PDF-Chatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Mistral API key:

```env
MISTRAL_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

1. Upload a PDF file.
2. The PDF is split into smaller text chunks.
3. Text chunks are converted into embeddings.
4. The embeddings are stored in a Chroma vector database.
5. Relevant chunks are retrieved based on your question.
6. Mistral AI generates an answer using the retrieved context.

## Example Questions

* Summarize this PDF.
* What is the main topic?
* Explain a specific chapter.
* List the important points.
* What does the document say about a particular topic?

## Limitations

* Supports PDF files only.
* Answers are based only on the uploaded document.
* Large PDFs may take a little longer to process.

## Future Improvements

* Support multiple PDFs
* Display source page numbers
* Add chat history memory
* Improve retrieval quality

## Author
Omm Kishor Tripathy
