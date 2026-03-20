from src.retriever import VectorStore
from src.generator import generate_answer

class LeadershipAgent:
    def __init__(self, vectorstore):
        self.vs = vectorstore
    
    def answer(self, query):
        docs = self.vs.retrieve(query)

        context = "\n\n".join(docs)

        answer = generate_answer(query, context)

        return {
            "query" : query,
            "retrieved_docs" : docs,
            "answer" : answer
        }