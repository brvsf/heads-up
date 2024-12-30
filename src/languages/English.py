import streamlit as st
from src.package.llm import LLMIntegration
from src.package.utils import StreamlitUI, StreamlitSession, TemplateFormat


def main():

    if not st.session_state['categories'] and not st.session_state['difficulty']:
        StreamlitUI.options(language='English')

    with st.sidebar:
        st.header("Menu")

        if st.button("🔧 Options"):
            StreamlitUI.options(language="English")


        if st.button("🕹️ How to play"):
            StreamlitUI.how_to_play(language="English")

        if st.button("💬 Change language"):
            StreamlitSession.reset_session_state()
            st.rerun()

    # Model configuration
    client = LLMIntegration.model(model="gpt-4") # gpt-4 / gpt-3.5-turbo
    formated_prompt = TemplateFormat.format_en(
        st.session_state['categories'],
        st.session_state['difficulty']
    )

    StreamlitSession.session_conversation_chain(client, prompt= formated_prompt)

    conversation_chain = st.session_state["conversation_chain"]

    # Show message history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Capture user input
    if user_message := st.chat_input("Start guessing"):
        # Adiciona a mensagem do usuário ao histórico
        st.session_state["messages"].append({"role": "user", "content": user_message})

        # Process message with langchain
        ai_response = conversation_chain.run(input=user_message)

        # Shows user messages
        st.chat_message("user").markdown(user_message)

        # Show GuessMaster messages
        with st.chat_message("ai"):
            st.markdown(ai_response)

        # Adds new messages to the message history
        st.session_state["messages"].append({"role": "ai", "content": ai_response})


if __name__ == "__main__":
    main()
