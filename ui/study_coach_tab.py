import streamlit as st
from core.study_coach.planner_agent import create_study_plan
from core.study_coach.teacher_agent import explain_topic
from core.study_coach.examiner_agent import ask_question, check_answer
from core.study_coach.weakness_detector import detect_weakness 
from core.study_coach.motivator_agent import motivate_user

def show_study_coach(llm):
    st.header("🎯 Personal Study Coach")
    st.write("I'm your AI study buddy! I'll help you plan, learn, test yourself, and stay motivated.")

    topic = st.text_input("What do you want to learn today?", placeholder="e.g., Python loops, World War II, Calculus")

    if st.button("Start Learning Session", type="primary"):
        if not topic.strip():
            st.warning("Please enter a topic!")
            return
        
        with st.spinner("Creating your study plan..."):
            plan = create_study_plan(llm,topic)

        st.markdown("###  Your Study Plan")
        st.write(plan)

        st.markdown("###  Let's Learn!")
        explanation = explain_topic(llm, topic)
        st.write(explanation)

        st.markdown("###  Time for a Quiz!")
        question = ask_question(llm,topic)
        st.session_state.current_question = question
        st.write("**Question:** " + question)
        
        user_answer = st.text_input("Your answer:")
        if st.button("Check answer"):
            if user_answer:
                feedback = check_answer(llm,topic,st.session_state.current_question,user_answer)
                st.write(feedback)

                if "wrong" in feedback.lower() or "incorrect" in feedback.lower() or "not quite" in feedback.lower():
                    with st.spinner("Analyzing your weak areas..."):
                        weakness = detect_weakness(llm,topic,st.session_state.current_question,user_answer,feedback)
                        
                    st.markdown("###  Areas to Improve")
                    st.warning(weakness)

                motivation = motivate_user(llm, feedback)
                st.markdown("###  Keep Going!")
                st.success(motivation)
            else:
                st.warning("Please write your answer first!")

