def run_judge_agent(llm, topic, pro_args, contra_args, risks):
    prompt = f"""
    You are the final judge. You have read:
    - Arguments in favor
    - Arguments against
    - Risk analysis

    Now give a balanced final recommendation.
    Say clearly: Yes, No, or Maybe with conditions?
    Explain your reasoning in 4-6 sentences.

    Topic: {topic}
    Pro: {pro_args}
    Contra: {contra_args}
    Risks: {risks}

    Final recommendation:
    """
    response = llm.invoke(prompt)
    return response.content