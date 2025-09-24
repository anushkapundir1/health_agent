from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_analysis(user_id, report_text, ai_result):
    """Save AI analysis into Supabase table"""
    response = supabase.table("analysis_history").insert({
        "user_id": user_id,
        "report_text": report_text,
        "ai_result": ai_result
    }).execute()
    return response

def fetch_history(user_id):
    """Fetch previous analyses for a user"""
    response = supabase.table("analysis_history").select("*").eq("user_id", user_id).execute()
    return response.data
