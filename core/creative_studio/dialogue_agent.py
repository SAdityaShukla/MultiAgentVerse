def create_dialogue(llm, story):
    prompt = f"""
    You are a dialogue expert.
    Take this story:
    {story}
    
    Add 5-7 lines of natural, emotional dialogue between characters.
    Make it fit perfectly into the story.
    Show character names and emotions.
    
    Dialogue:
    """
    response = llm.invoke(prompt)
    return response.content