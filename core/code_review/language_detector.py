def detect_language(llm, code):
    """
    Detects the primary programming language from the code snippet.
    Returns a string like "Python", "JavaScript", "Java", etc.
    """
    prompt = f"""
    You are an expert code language detector.
    Look at this code snippet and tell me the **main programming language**.
    Respond with **only** the language name (e.g., "Python", "JavaScript", "C++", "Java", "Go", "Rust", "HTML", etc.).
    If mixed, pick the dominant one.
    If impossible to tell, say "Unknown".

    Code:
    {code[:1500]}  # Limit to first 1500 chars for speed

    Language:
    """
    response = llm.invoke(prompt)
    lang = response.content.strip()
    
    lang = lang.replace("**", "").replace("`", "").strip()
    return lang if lang else "Unknown"