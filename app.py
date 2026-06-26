import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="📚 AI Book Chat", page_icon="🤖", layout="wide")

st.title("📚 AI Book Chat Assistant")
st.markdown("Upload a PDF book and chat with it like ChatGPT 💬")

# ===============================
# SIDEBAR - FILE UPLOAD
# ===============================
with st.sidebar:
    st.header("⚙️ Setup")

    uploaded_file = st.file_uploader("📁 Upload your PDF book", type="pdf")

    if uploaded_file:
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("PDF uploaded successfully!")

# ===============================
# SESSION STATE INIT
# ===============================
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ===============================
# BUILD VECTOR DB
# ===============================
def build_vector_db(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vectorstore

# ===============================
# LOAD MODEL + PROMPT
# ===============================
model = ChatMistralAI(model="mistral-small-latest")

template = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful AI assistant. Use ONLY the provided context. "
     "If answer is not present, say you could not find it."),
    ("human", "Context: {context}\nQuestion: {question}")
])

# ===============================
# PROCESS PDF BUTTON
# ===============================
if uploaded_file and st.session_state.vectorstore is None:
    with st.spinner("""
    📊 Processing book and creating embeddings...
    If the file is too long, it may take a few minutes to load.
    """):
        st.session_state.vectorstore = build_vector_db(f"temp_{uploaded_file.name}")
    st.success("✅ Knowledge base ready! Start chatting below.")

# ===============================
# CHAT INTERFACE
# ===============================
if st.session_state.vectorstore:

    retriever = st.session_state.vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.75}
    )

    # Chat display
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(msg)

    # User input
    user_query = st.chat_input("Ask something from your book...")

    if user_query:
        # store user msg
        st.session_state.chat_history.append(("user", user_query))

        with st.chat_message("user"):
            st.write(user_query)

        # Retrieve context
        docs = retriever.invoke(user_query)
        context = "\n".join([d.page_content for d in docs])

        prompt = template.format_messages(
            context=context,
            question=user_query
        )

        with st.chat_message("assistant"):
            with st.spinner("Thinking... 🤔"):
                response = model.invoke(prompt)
                answer = response.content
                st.write(answer)

        st.session_state.chat_history.append(("assistant", answer))

else:
    st.info("⬅️ Upload a PDF in the sidebar to begin chatting.")