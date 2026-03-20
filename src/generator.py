from groq import Groq
from config import groq_api_key

client = Groq(api_key=groq_api_key)

def generate_answer(query, context):
    
    prompt = f"""
            You are a Senior Business Analyst presenting to the C-Suite.
            
            Context: {context}
            Question: {query}

            Instructions:
            1. Provide a "High-Level Executive Summary".
            2. Create a "Key Evidence" section with bullet points and specific figures (%, $, dates).
            3. Include a "Source Attribution" (e.g., 'Per the Q1 Operations Update').
            4. If the data is missing, state 'Information not available in current internal documents.'
            """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content