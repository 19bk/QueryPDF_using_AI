import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

# import os

# # Print all environment variables
# for key, value in os.environ.items():
#     print(key, value)  # Remember to remove this after checking



st.set_page_config(page_title="Chat with your PDFs", page_icon=":books:")

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text
    
def get_text_chunks(raw_text):
    text_splitter  = CharacterTextSplitter(separator="/n",
                                            chunk_size=1000, chunk_overlap =200, length_function=len)
    chunks=text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)  # Corrected FAISS usage
    return vectorstore


def main():
    load_dotenv()
    st.header("Chat with your PDFs :books:")
    st.text_input("Ask a question about your PDFs:")

with st.sidebar:
    st.subheader("Your Docs")
    pdf_docs = st.file_uploader("Upload PDFs here", accept_multiple_files=True)
    if st.button("Process"):
        with st.spinner("processing"):
        # get pdf text
            raw_text = get_pdf_text(pdf_docs)
            # st.write(raw_text)

        # get text chunks
            text_chunks = get_text_chunks(raw_text)
            st.write(text_chunks)
# create vector store
            vectorstore = get_vectorstore(text_chunks)


if __name__=='__main__':
    main()