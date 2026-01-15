def read_code(llm, code, language):
    prompt = f"""
    You are an expert code reader in {language}.
    Read this code and give a brief summary:
    - Primary language/framework (confirm: {language})
    - Main purpose/function of the code
    - Key components (functions/classes/modules)
    - Overall structure and complexity

    Code:
    {code}

    Summary:
    """
    response = llm.invoke(prompt)
    return response.content.strip()