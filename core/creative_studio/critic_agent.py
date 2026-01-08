def give_critique(llm, story, dialogue):
    prompt = f"""
    You are a tough but fair critic.
    Story: {story}
    Dialogue: {dialogue}
    
    Give honest feedback:
    - What works well
    - What could be better
    - Suggestions for improvement
    Be constructive and encouraging.
    
    Critique:
    """
    response = llm.invoke(prompt)
    return response.content