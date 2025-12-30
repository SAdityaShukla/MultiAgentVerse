def run_contra_agent(llm, topic):
    prompt = f"""
    You are a critical thinker. Your job is to argue AGAINST this decision.
    Give 4-5 clear, logical reasons why this might be a bad idea.
    Be honest and point out real risks or downsides.

    Topic: {topic}

    Your arguments:
    """
    response = llm.invoke(prompt)
    return response.content