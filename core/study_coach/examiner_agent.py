def ask_question(llm, topic):
    prompt = f"""
    You are a fair examiner.
    Create one good multiple-choice question about: {topic}
    Include 4 options (A, B, C, D) and mark the correct one with (Correct)
    
    Example format:
    What is photosynthesis?
    A) Breathing
    B) Eating
    C) Process by which plants make food using sunlight (Correct)
    D) Sleeping
    
    Question:
    """
    response = llm.invoke(prompt)
    return response.content

def check_answer(llm, topic, question, user_answer):
    prompt = f"""
    You are a teacher checking an answer.
    Topic: {topic}
    Question: {question}
    Student's answer: {user_answer}
    
    Tell them:
    - If they are correct or wrong
    - The correct answer if wrong
    - A short explanation why
    
    Be encouraging even if wrong.
    
    Feedback:
    """
    response = llm.invoke(prompt)
    return response.content