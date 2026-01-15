import streamlit as st
from core.creative_studio.idea_generator import generate_ideas
from core.creative_studio.story_builder import build_story
from core.creative_studio.dialogue_agent import create_dialogue
from core.creative_studio.critic_agent import give_critique
from core.creative_studio.polisher_agent import polish_final

def show_creative_studio(llm):
    st.header(" Creative Studio")
    st.write("Let's create something amazing! Give me an idea, and I'll help you turn it into a polished story.")

    user_idea = st.text_input("What's your basic idea or theme?", 
                              placeholder="e.g., Last man standing, A magical forest adventure, A time-travel mystery")
    
    if st.button("Start Creation", type="primary"):
        if not user_idea.strip():
            st.warning("Please enter your idea first!")
            return
        
        with st.spinner("Generating ideas..."):
            ideas = generate_ideas(llm, user_idea)

        st.markdown("###  Brainstormed Ideas")
        st.write(ideas)

        st.markdown("###  Full Story")
        with st.spinner("Building the story..."):
            story = build_story(llm, ideas)
        st.write(story)

        st.markdown("###  Dialogue")
        with st.spinner("Adding lively dialogue..."):
            dialogue = create_dialogue(llm, story)
        st.write(dialogue)

        st.markdown("###  Critic's Feedback")
        with st.spinner("Critiquing the work..."):
            critique = give_critique(llm, story, dialogue)
        st.write(critique)

        st.markdown("###  Final Polished Version")
        with st.spinner("Polishing everything..."):
            polished = polish_final(llm, story, dialogue, critique)
        st.success(polished)

        st.download_button("Download Final Story", polished, file_name="creative_story.txt")
