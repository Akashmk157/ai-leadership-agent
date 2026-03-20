from src.ingest import load_documents, split_documents
from src.retriever import VectorStore
from src.agent import LeadershipAgent

def main():
    print("AI Leadership Insight Agent")

    #Loading documents
    docs = load_documents("data/reports")

    #Splitting the chunks
    chunks = split_documents(docs)

    #Build vectorDB
    vs = VectorStore()
    vs.build_index(chunks)

    #Create agent
    agent = LeadershipAgent(vs)

    while True:
        query = input("\n Enter your question (or type 'exit'): ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        response = agent.answer(query)

        print("\n" + "="*60)
        print(f"Question: {query}\n")

        # print("Retrieved Context:\n")
        # for i, doc in enumerate(response["retrieved_docs"], 1):
        #     print(f"{i}. {doc[:200]}\n")

        print("Answer:\n")
        print(response["answer"])
        print("="*60)


if __name__ == "__main__":
    main()