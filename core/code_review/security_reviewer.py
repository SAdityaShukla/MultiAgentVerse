def check_security(llm, code, language):
    prompt = f"""
    You are a security auditor specializing in {language}.
    Review this code for vulnerabilities common in {language}:
    - Injection attacks (SQL, command, etc.)
    - Hard-coded secrets / API keys
    - Unsafe input handling
    - File/path traversal
    - Insecure deserialization or eval/exec
    - Buffer overflows (C/C++), prototype pollution (JS), etc.

    Code:
    {code}

    Security issues:
    List them with:
    - Approximate line number
    - Description
    - Severity (Low / Medium / High / Critical)
    """
    response = llm.invoke(prompt)
    return response.content.strip()