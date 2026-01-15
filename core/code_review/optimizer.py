def suggest_optimizations(llm, code, summary, language):
    prompt = f"""
    You are a performance expert in {language}.
    Code summary: {summary}
    Code:
    {code}

    Suggest performance optimizations specific to {language}:
    - Time/space complexity improvements
    - Better algorithms or data structures
    - Avoid repeated work (caching, memoization, etc.)
    - {language}-specific best practices (e.g., list comprehensions in Python, streams in Java)

    List 3-6 concrete suggestions with approximate line numbers.

    Optimizations:
    """
    response = llm.invoke(prompt)
    return response.content.strip()