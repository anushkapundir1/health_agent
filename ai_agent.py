import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-8b-8192",   # stable model
    temperature=0.3,
    max_tokens=1024
)

def analyze_report(report_text):
    prompt = f"""
You are a professional medical assistant.
Analyze the following medical report and provide:
1. Summary
2. Key health concerns
3. Normal vs abnormal values
4. Simple health advice

Medical Report:
{report_text}
"""
    return llm.invoke(prompt).content
