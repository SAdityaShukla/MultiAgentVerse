import streamlit as st
from core.code_review.language_detector import detect_language
from core.code_review.reader_agent import read_code
from core.code_review.bug_finder import find_bugs
from core.code_review.optimizer import suggest_optimizations
from core.code_review.security_reviewer import check_security
from core.code_review.final_reviewer import generate_final_review


def show_code_review(llm):
    st.header("Smart Code Reviewer")
    st.write("Paste your code below. It will be reviewed to: find bugs, improve style, optimize performance, check security, and suggest fixes.")

    code = st.text_area("Paste your code here", height=300, placeholder="# Your code...")

    if st.button("Review My Code", type="primary"):
        if not code.strip():
            st.warning("Please paste some code first!")
            return
        
    
        with st.spinner("Detecting language..."):
            language = detect_language(llm, code)
            st.info(f"Detected language: **{language}**")

        with st.spinner("Reading and analyzing your code..."):
            code_summary = read_code(llm, code, language)
        
        st.markdown("### Code Summary")
        st.write(code_summary)

        with st.spinner("Finding bugs..."):
            bugs = find_bugs(llm, code, code_summary, language)

        st.markdown("### Bugs & Logical Issues")
        st.write(bugs)

        with st.spinner("Checking performance..."):
            optimizations = suggest_optimizations(llm, code, code_summary, language)

        st.markdown("###  Performance Suggestions")
        st.write(optimizations)

        with st.spinner("Scanning for security risks..."):
            security = check_security(llm, code, language)

        st.markdown("###  Security Review")
        st.write(security)

        with st.spinner("Preparing final review..."):
            final_report = generate_final_review(llm, code_summary, bugs, optimizations, security, language)

        st.markdown("###  Final Review Report")
        st.success(final_report)
