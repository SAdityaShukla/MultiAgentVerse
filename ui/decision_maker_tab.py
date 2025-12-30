import streamlit as st
from core.decision_maker.pro_agent import run_pro_agent
from core.decision_maker.contra_agent import run_contra_agent
from core.decision_maker.risk_analyst import run_risk_analyst
from core.decision_maker.judge_agent import run_judge_agent


def show_decision_maker(llm):
    st.header("⚖️ Decision Maker")
    st.write("Tell me your decision or dilemma. This agent will debate both sides, analyze risks, and give a final judgment.")

    user_input = st.text_input("What decision are you thinking about?", placeholder="e.g., Should I change my job?")

    if st.button("Start debate"):
        if not user_input:
            st.warning("Please enter a decision or dilemma.")
            return
        
        with st.spinner("Pro Agent is thinking"):
            pro = run_pro_agent(llm, user_input)

        with st.spinner("Contra Agent is thinking"):
            contra = run_contra_agent(llm, user_input)

        with st.spinner("Risk Analyst is thinking"):
            risks = run_risk_analyst(llm,user_input,pro, contra)

        with st.spinner("Judge Agent is thinking"):
            judgment = run_judge_agent(llm, user_input, pro, contra, risks)

        st.markdown("###  Arguments For")
        st.write(pro)

        st.markdown("###  Arguments Against")
        st.write(contra)

        st.markdown("###  Risk Analysis")
        st.write(risks)

        st.markdown("###  Final Judgment")
        st.success(judgment)







