import streamlit as st
from core.study_coach.planner_agent import create_study_plan
from core.study_coach.teacher_agent import explain_topic
from core.study_coach.examiner_agent import ask_question, check_answer
from core.study_coach.weakness_detector import detect_weakness
from core.study_coach.motivator_agent import motivate_user

def show_study_coach(llm):
    st.header(" Personal Study Coach")
    st.write("I'm your AI study buddy! I'll help you plan, learn, test yourself, and stay motivated.")

    if "study_topic" not in st.session_state:
        st.session_state.study_topic = ""
    if "study_plan" not in st.session_state:
        st.session_state.study_plan = ""
    if "study_explanation" not in st.session_state:
        st.session_state.study_explanation = ""
    if "current_question" not in st.session_state:
        st.session_state.current_question = ""


    topic = st.text_input(
        "What do you want to learn today?",
        placeholder="e.g., Python loops, World War II, Calculus"
    )

  
    if st.button("Start Learning Session", type="primary"):
        if not topic.strip():
            st.warning("Please enter a topic!")
            return

        
        st.session_state.study_topic = topic

        
        with st.spinner("Creating your study plan..."):
            plan = create_study_plan(llm, topic)
        st.session_state.study_plan = plan

        with st.spinner("Preparing explanation..."):
            explanation = explain_topic(llm, topic)
        st.session_state.study_explanation = explanation

        with st.spinner("Making a quiz question..."):
            question = ask_question(llm, topic)
        st.session_state.current_question = question

        st.rerun() 

    
    if st.session_state.study_plan:
        st.markdown("###  Your Study Plan")
        st.write(st.session_state.study_plan)

    if st.session_state.study_explanation:
        st.markdown("###  Let's Learn!")
        st.write(st.session_state.study_explanation)

    if st.session_state.current_question:
        st.markdown("###  Time for a Quiz!")
        st.write("**Question:** " + st.session_state.current_question)

        user_answer = st.text_input("Your answer:")

        if st.button("Check Answer"):
            if not user_answer.strip():
                st.warning("Please write your answer first!")
            else:
                feedback = check_answer(
                    llm,
                    st.session_state.study_topic,
                    st.session_state.current_question,
                    user_answer
                )
                st.markdown("**Feedback:**")
                st.write(feedback)

                if any(word in feedback.lower() for word in ["wrong", "incorrect", "mistake","unfortunately"]):
                    with st.spinner("Finding weak areas..."):
                        weakness = detect_weakness(
                            llm,
                            st.session_state.study_topic,
                            st.session_state.current_question,
                            user_answer,
                            feedback
                        )
                    st.markdown("###  Areas to Improve")
                    st.warning(weakness)

                motivation = motivate_user(llm, feedback)
                st.markdown("###  Keep Going!")
                st.success(motivation)