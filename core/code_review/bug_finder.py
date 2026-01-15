def find_bugs(llm, code, summary, language):
    prompt = f"""
    You are an expert bug hunter in {language}.
    Code summary: {summary}
    Code:
    {code}

    Find all bugs, logical errors, edge cases, or potential crashes common in {language}.
    Include {language}-specific issues (e.g., null pointer dereference in Java, undefined behavior in C++, prototype pollution in JavaScript).

    List them clearly with:
    - Approximate line number
    - Description of the bug
    - Severity (Low / Medium / High / Critical)

    Bugs found:
    """
    response = llm.invoke(prompt)
    return response.content.strip()