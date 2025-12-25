import streamlit as st
from config import get_llm, get_embeddings

st.set_page_config(page_title="MultiAgentVerse", page_icon="🤖", layout="centered")
st.title("MultiAgentVerse")
st.markdown("**Powerful AI agents for learning, decision-making, coding, and creativity**")
st.divider()


with st.sidebar:
    st.header("🔑 API Key")
    groq_api_key = st.text_input(
        "Groq API Key",
        type="password",
        help="Get free key at https://console.groq.com/keys"
    )

if not groq_api_key:
    st.warning("Please enter your Groq API key in the sidebar.")
    st.stop()

llm = get_llm(groq_api_key)
embeddings = get_embeddings()


if "current_task" in st.session_state and st.session_state.current_task:
    task = st.session_state.current_task

    if st.button("← Back to Home"):
        st.session_state.current_task = None
        st.rerun()

    if task == "exam_ready":
        from ui.exam_ready_tab import show_exam_ready
        show_exam_ready(llm, embeddings)
     
    elif task == "decision_maker":
        from ui.decision_maker_tab import show_decision_maker
        show_decision_maker(llm)

    elif task == "study_coach":
        from ui.study_coach_tab import show_study_coach
        show_study_coach(llm)

    elif task == "code_review":
        from ui.code_review_tab import show_code_review
        show_code_review(llm,embeddings)

    elif task == "creative_studio":
        from ui.creative_studio_tab import show_creative_studio
        show_creative_studio(llm)


else:
    st.markdown("### Choose a task")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)


    with col1:
        if st.button("📚 Exam Ready Material", use_container_width=True, type="primary"):
            st.session_state.current_task = "exam_ready"
            st.rerun()


    with col2:
        if st.button("⚖️ Decision Maker", use_container_width=True, type="primary"):
            st.session_state.current_task = "decision_maker"
            st.rerun()


    with col3:
        if st.button("🎯 Study Coach", use_container_width=True, type="primary"):
            st.session_state.current_task = "study_coach"
            st.rerun()



    with col4:
        if st.button("🔍 Code Review & Refactor", use_container_width=True, type="primary"):
            st.session_state.current_task = "code_review"
            st.rerun()



    col_center = st.columns([1, 2, 1])[1]  
    with col_center:
        if st.button("✨ Creative Studio", use_container_width=True, type="primary"):
            st.session_state.current_task = "creative_studio"
            st.rerun()

