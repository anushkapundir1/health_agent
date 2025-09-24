from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_report(report_text):
    """Analyze health report using Groq LLM"""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # Groq fast LLaMA model
            messages=[
                {"role": "system", "content": "You are a helpful AI health assistant."},
                {"role": "user", "content": f"Analyze this health report:\n\n{report_text}"}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing report: {e}"
