import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.texts = []
    
    def build_index(self, chunks):
        self.texts = chunks
        embeddings = self.model.encode(chunks)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))
    
    def retrieve(self, query, k=5):
        query_embeddings = self.model.encode([query])
        dis, ind = self.index.search(query_embeddings, k)

        results = [self.texts[i] for i in ind[0]]

        unique_results = list(dict.fromkeys(results))
        return unique_results