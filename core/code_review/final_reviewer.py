def generate_final_review(llm, code_summary, bugs, optimizations, security, language):
    prompt = f"""
    You are the lead code reviewer for {language} projects.
    Summarize the entire review:

    Code summary: {code_summary}
    Bugs found: {bugs}
    Performance optimizations: {optimizations}
    Security issues: {security}

    Final report should include:
    - Overall score (1-10)
    - Key strengths
    - Top 3-5 issues to fix first (prioritized)
    - Final recommendation (e.g., "Ready for production", "Needs fixes", "Major rewrite required")
    - Any {language}-specific advice

    Final review report:
    """
    response = llm.invoke(prompt)
    return response.content.strip()