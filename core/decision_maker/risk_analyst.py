def run_risk_analyst(llm, topic, pro_args, contra_args):
    prompt = f"""
    You are a risk analyst. Read the pro and contra arguments below.
    List the top 3-5 real risks or challenges if this decision is made.
    Be practical and specific.

    Topic: {topic}
    Pro arguments: {pro_args}
    Contra arguments: {contra_args}

    Top risks:
    """
    response = llm.invoke(prompt)
    return response.content