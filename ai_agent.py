import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_report(report_text):
    prompt = f"""
You are a professional medical assistant.

Analyze the following medical report and provide:

1. Summary of the report
2. Key health concerns (if any)
3. Normal vs Abnormal values in bullet points
4. Simple health advice for the patient

Medical Report:
{report_text}
"""

    chat = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1024,
    )

    return chat.choices[0].message.content
