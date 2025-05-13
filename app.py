"""
Streamlit UI for the autonomous task execution agent.
This app accepts user tasks in natural language, sends them to the LangChain agent,
and displays the agent's response in the browser.
"""

import streamlit as st
from agent_core import run_agent

def main():
    """
    Renders the Streamlit interface and handles user input/output for the agent.

    """
    # Set up the Streamlit page
    st.set_page_config(page_title="Autonomous AI Agent", page_icon="🤖")
    st.title("🤖 Autonomous Task Execution Agent")

    st.markdown(
        "Enter a task in natural language — the agent will reason, choose tools, "
        "and complete the task for you."
    )

    # Text input for the user's task
    task = st.text_area("What should I do?", placeholder="e.g. What is 42 * 19? or Summarize AI trends")

    # Run the agent when the button is clicked
    if st.button("Run Agent"):
        if not task.strip():
            st.warning("Please enter a valid task.")
        else:
            with st.spinner("Thinking..."):
                try:
                    response = run_agent(task)
                    st.success("Task completed successfully!")
                    st.markdown(f"**Result:**\n\n{response}")
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    main()