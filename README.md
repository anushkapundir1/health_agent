# 🏥 Health Assisting Agent

## Overview
Health Assisting Agent is a secure AI-powered application designed to analyze
medical PDF reports and provide structured, LLM-assisted interpretations.
The system helps users understand lengthy medical documents using
advanced language models while ensuring secure data handling.

The project focuses on combining **Generative AI**, **secure authentication**,
and **document analysis** into a single end-to-end application.



## Key Features
- Upload and analyze PDF medical reports
- LLM-powered interpretation of medical content
- Text chunking and summarization for long documents
- Secure user authentication and session management
- Storage of analysis history for future reference



## Tech Stack
- Python
- Streamlit
- Supabase (Authentication + PostgreSQL)
- Groq LLaMA API


## How It Works
1. User securely logs in using Supabase authentication
2. Medical PDF is uploaded and parsed
3. Text is split into manageable chunks
4. LLM processes each chunk for better accuracy
5. Summarized insights are generated and stored securely



## Learning Outcomes
- Building secure AI applications
- Integrating LLM APIs for real-world use cases
- Handling sensitive data responsibly
- Improving document analysis through chunking and summarization



## Future Enhancements
- Medical disclaimer and safety layers
- Improved UI/UX for report visualization
- Support for additional medical document formats
