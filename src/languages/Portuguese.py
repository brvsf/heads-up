import streamlit as st
from src.package.llm import LLMIntegration
from src.package.utils import StreamlitUI, StreamlitSession


def main():


    if not st.session_state['categories'] and not st.session_state['difficulty']:
        StreamlitUI.options(language='Portuguese')

    with st.sidebar:
        st.header("Menu")

        if st.button("🔧 Opções"):
            StreamlitUI.options(language="Portuguese")

        if st.button("🕹️ Como jogar"):
            StreamlitUI.how_to_play(language="Portuguese")

        if st.button("ℹ️ Sobre o projeto"):
            st.switch_page("AboutUsPT.py")

        if st.button("💬 Trocar idioma"):
            StreamlitSession.reset_session_state()
            st.rerun()


    # Model configuration
    client = LLMIntegration.model(model="gpt-4") # gpt-4 / gpt-3.5-turbo

    if st.session_state['prompt']:
        StreamlitSession.session_conversation_chain(client, prompt=st.session_state['prompt'])
        if st.session_state['prompt'] != st.session_state["conversation_chain"].memory.chat_memory.messages[0].content:
            LLMIntegration.update_prompt(st.session_state["conversation_chain"], st.session_state['prompt'])

    conversation_chain = st.session_state["conversation_chain"]

    # Initial bot message
    with st.chat_message("ai"):
        st.markdown(
            f"""Você selecionou a categoria: {', '.join(st.session_state['categories'])}
            e dificuldade: {st.session_state['difficulty']}
            \nComece a adivinhar!"""
            )
    # Show message history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Capture user input
    if user_message := st.chat_input(st.session_state["chat_label"], disabled=st.session_state["disable_chat"]):
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

        if "Parabéns!" in ai_response:
            st.session_state["disable_chat"] = True
            st.session_state["chat_label"] = "Você já acertou!"
            st.rerun()



if __name__ == "__main__":
    main()
