def motivate_user(llm, feedback):
    prompt = f"""
    You are a positive and energetic motivator.
    The student just got this feedback: {feedback}
    
    Give them an encouraging message to keep going.
    Make it warm, personal, and inspiring.
    Keep it short (3-5 sentences).
    
    Motivation:
    """
    response = llm.invoke(prompt)
    return response.content