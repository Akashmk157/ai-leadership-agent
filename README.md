# AI Leadership Insight & Decision Agent
## Overview

This project implements an AI-powered Leadership Insight Agent that can:

- Analyze internal company documents (reports, operations, strategy)

- Answer leadership-level questions about:

    - Revenue trends

    - Department performance

    - Key risks 

- Generate concise, structured, and fact-based leadership insights grounded in documents

The system is built using a Retrieval-Augmented Generation (RAG) pipeline.

---

## Objective

Build an AI agent that:

- Ingests and processes company documents

- Retrieves relevant information for a query

- Generates accurate answers grounded in the documents

---

## Assumptions

Since no dataset was provided, I created a synthetic dataset simulating real enterprise documents:

- Quarterly reports (Q1, Q2)

- Operational updates

- Annual reports

All answers are generated strictly based on these documents.


---

## Architecture

```text
Company Documents
        ↓
Document Ingestion
        ↓
Chunking (500 size, 100 overlap)
        ↓
Embeddings (MiniLM)
        ↓
FAISS Vector Store
        ↓
Retriever (Top-K search)
        ↓
LLM (LLaMA 3.1 via Groq)
        ↓
Structured Leadership Answer
```
---

## Design Decisions

- Chunk Size = 500, Overlap = 100 : Preserves context across chunk boundaries

- FAISS : Efficient similarity search

- MiniLM Embeddings : Lightweight and fast

- Top-K = 3 : Reduces noise and improves relevance

- Prompt Engineering : Ensures structured and grounded output

- Duplicate Removal : Improves answer quality

---

## Workflow

Documents are loaded and split into chunks

Each chunk is converted into embeddings

FAISS index is built

For a query:

- Relevant chunks are retrieved

- Context is passed to LLM

- LLM generates a structured response


---

## Example Queries

1) What is our current revenue trend?

2) Which departments are underperforming?

3) What were the key risks highlighted in the last quarter?


## Sample Outputs
### 1) Revenue Trend
Summary:
Revenue increased by 12% in Q1 and 8% in Q2, showing continued but slowing growth.

Insight:
Strong performance observed in APAC region.


### 2) Underperforming Departments
Summary:
Logistics and Customer Support are underperforming.

 Underperforming Departments:
- Logistics  
  - Delays due to supply chain issues  
- Customer Support  
  - Customer satisfaction dropped by 8%  

Strong Performing Departments:
- Engineering  
- Marketing  
  - Customer acquisition increased by 15%



### 3) Key Risks (Last Quarter)
Key Risks (Last Quarter - Q2):

- Infrastructure costs rising  
- Attrition in support teams

---
# Screen shots of working system
<img width="1911" height="900" alt="Screenshot 2026-03-20 053011" src="https://github.com/user-attachments/assets/f5f1c63f-56cd-42b7-b452-a926bb2d4732" />
<img width="1915" height="888" alt="Screenshot 2026-03-20 054229" src="https://github.com/user-attachments/assets/9d72535d-157b-4325-8cf6-5f9e0865033a" />
<img width="1910" height="912" alt="Screenshot 2026-03-20 054309" src="https://github.com/user-attachments/assets/361efc69-55a7-49ec-9215-065e72b2a26d" />
<img width="1915" height="863" alt="Screenshot 2026-03-20 054429" src="https://github.com/user-attachments/assets/924decc9-490d-4ccf-9422-63cf1705e17a" />

---

## Evaluation Approach

The system is evaluated using predefined leadership queries:

- Relevance of retrieved documents

- Accuracy of generated answers

- Clarity and structure of responses



## How to run

```bash
# Clone repo
git clone <repo-link>

cd ai-leadership-agent

# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set API key
set GROQ_API_KEY=your_api_key

# Run
python main.py
```

## Tech Stack

Python

Sentence Transformers (MiniLM)

FAISS

Groq (LLaMA 3.1)

LangChain (text splitting)

---

## Future Enhancement: Autonomous Decision Agent

The current system focuses on answering factual leadership queries using a RAG pipeline.

It can be extended into an autonomous decision-making system with:

- Multi-step reasoning to handle complex strategic queries  
- Cross-document analysis to identify trends and risks  
- Decision generation with actionable insights  

### Example:

**Query:** What should leadership prioritize?

**Output:**
- Improve logistics efficiency to reduce delays  
- Expand customer support to handle increased demand  
- Optimize infrastructure costs  

This evolution transforms the system from a Q&A assistant into a strategic AI advisor.
