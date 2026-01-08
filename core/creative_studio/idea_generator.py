def generate_ideas(llm, user_idea):
    prompt = f"""
    You are a creative brainstormer.
    Given this basic idea: "{user_idea}"
    
    Generate 3-5 exciting, original story ideas.
    Make them unique, fun, and full of potential.
    Number them 1 to 5.
    
    Ideas:
    """
    response = llm.invoke(prompt)
    return response.content