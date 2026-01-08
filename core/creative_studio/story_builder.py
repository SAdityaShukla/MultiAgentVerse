def build_story(llm, ideas):
    prompt = f"""
    You are a master storyteller.
    Choose the best idea from these brainstormed ideas:
    {ideas}
    
    Write a complete short story (400-600 words) based on the best one.
    Make it engaging, with beginning, middle, and end.
    Add vivid descriptions and emotions.
    
    Full story:
    """
    response = llm.invoke(prompt)
    return response.content