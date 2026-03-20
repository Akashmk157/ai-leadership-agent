import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(path):
    docs = []
    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
            docs.append(f.read())
    return docs


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap=100
    )
    chunks = []
    for doc in documents:
        chunks.extend(splitter.split_text(doc))
    return chunks
