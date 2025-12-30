def run_pro_agent(llm,topic):
    prompt = f"""
    You are a strong advocate. Your job is to argue IN FAVOR of this decision.
    Give 4-5 clear, logical, and positive reasons why this is a good idea.
    Be persuasive but honest.

    Topic: {topic}

    Your arguments:
    """
    response = llm.invoke(prompt)
    return response.content

