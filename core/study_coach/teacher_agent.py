# core/study_coach/teacher_agent.py
def explain_topic(llm, topic):
    prompt = f"""
    You are a friendly and clear teacher.
    Explain the topic: {topic}
    Use simple language, examples, and analogies.
    Keep it engaging and easy to understand.
    Write about 300-400 words.
    
    Explanation:
    """
    response = llm.invoke(prompt)
    return response.content