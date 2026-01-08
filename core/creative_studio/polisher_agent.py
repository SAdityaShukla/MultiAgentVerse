def polish_final(llm, story, dialogue, critique):
    prompt = f"""
    You are a professional editor.
    Original story: {story}
    Dialogue: {dialogue}
    Critic feedback: {critique}
    
    Polish everything:
    - Fix grammar and flow
    - Improve descriptions
    - Integrate dialogue naturally
    - Apply critic suggestions
    Keep the length similar.
    
    Final polished version:
    """
    response = llm.invoke(prompt)
    return response.content