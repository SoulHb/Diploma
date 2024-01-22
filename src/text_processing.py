from langchain_community.document_loaders import PyPDFLoader
from config import *


def load_pdf(data_path):
    loader = PyPDFLoader(data_path)
    text = ''
    pages = loader.load()
    # Extract text
    for i in range(len(pages)):
        text += f"{pages[i].page_content}\n"
    return text
