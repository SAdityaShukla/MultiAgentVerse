def detect_weakness(llm, topic, question, user_answer, feedback):
    prompt = f"""
    You are a smart learning analyst.
    The student just answered a question wrong or partially wrong.
    
    Topic: {topic}
    Question: {question}
    Student's answer: {user_answer}
    Teacher's feedback: {feedback}
    
    Your job:
    - Find the main concept or skill the student is weak in
    - Suggest 1-2 specific things they should review or practice
    - Be kind and helpful, not harsh
    
    Keep it short and clear.
    
    Weak areas and advice:
    """
    response = llm.invoke(prompt)
    return response.content