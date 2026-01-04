# core/study_coach/planner_agent.py
def create_study_plan(llm, topic):
    prompt = f"""
    You are an expert study planner.
    Create a clear, step-by-step 7-day study plan for learning: {topic}
    Make it realistic for someone with 1-2 hours per day.
    Include daily goals and small milestones.
    
    Format as a numbered list with Day 1, Day 2, etc.
    
    Study plan:
    """
    response = llm.invoke(prompt)
    return response.content