import streamlit as st
from auth_service import login, signup
from pdf_extractor import extract_text_from_pdf
from ai_agent import analyze_report
from db_service import save_analysis, fetch_history

st.set_page_config(page_title="Health Agent", page_icon="⚕️")

st.title("⚕️ Health Assisting Agent")

menu = ["Login", "Signup", "Dashboard"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login(email, password)
        if user:
            st.success(f"Welcome {email} 🎉")
            st.session_state["user"] = email

elif choice == "Signup":
    st.subheader("Signup")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        user = signup(email, password)
        if user:
            st.success("Account created! Please log in.")

elif choice == "Dashboard":
    if "user" not in st.session_state:
        st.warning("Please log in first.")
    else:
        st.subheader("Upload and Analyze Health Report")

        uploaded_file = st.file_uploader("Upload PDF", type="pdf")

        if uploaded_file is not None:
            report_text = extract_text_from_pdf(uploaded_file)
            st.text_area("Extracted Text", report_text, height=200)

            if st.button("Analyze Report"):
                ai_result = analyze_report(report_text)
                st.success("AI Analysis:")
                st.write(ai_result)

                # Save to Supabase
                save_analysis(st.session_state["user"], report_text, ai_result)

        st.subheader("Your Previous Analyses")
        history = fetch_history(st.session_state["user"])
        if history:
            for row in history:
                st.markdown(f"""
                **Date:** {row['created_at']}  
                **Result:** {row['ai_result']}  
                ---
                """)
