import streamlit as st
from ingest import ingest_document
from qa_chain import answer_question

st.set_page_config(page_title="📄 Document Q&A Assistant")
st.title("📄 Document Q&A Assistant")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])
if uploaded_file:
    file_path = f"./data/uploads/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Document uploaded successfully.")
    ingest_document(file_path)

question = st.text_input("Ask a question about the document:")
if question:
    response, sources = answer_question(question)
    st.markdown("### 🧠 Answer")
    st.write(response)
    st.markdown("### 📚 Sources")
    for s in sources:
        st.markdown(f"> {s.page_content[:300]}...")

