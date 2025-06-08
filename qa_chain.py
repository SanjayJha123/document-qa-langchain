from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate

persist_dir = "./data/vectorstore"

retriever = FAISS.load_local(persist_dir, OpenAIEmbeddings()).as_retriever()
llm = OpenAI(temperature=0)

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are a helpful assistant. Use the context below to answer the question.
    
    Context:
    {context}

    Question:
    {question}

    Answer:
    """
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt_template}
)

def answer_question(question):
    result = qa_chain({"query": question})
    return result["result"], result["source_documents"]

