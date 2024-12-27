import streamlit as st
from src.package.utils import StreamlitUI, StreamlitSession, TemplateFormat
from src.package.llm import LLMIntegration


def main():

    if not st.session_state['categories'] and not st.session_state['difficulty']:
        StreamlitUI.options(language='Portuguese')

    with st.sidebar:
        if st.button("Opções"):
            StreamlitUI.options(language="Portuguese")
        if st.button("Trocar idioma"):
            StreamlitSession.reset_session_state()
            st.rerun()

    # Model configuration
    client = LLMIntegration.model(model="gpt-3.5-turbo") # gpt-4 / gpt-3.5-turbo
    formated_prompt = TemplateFormat.format_pt(
        st.session_state['categories'],
        st.session_state['difficulty']
    )

    StreamlitSession.session_conversation_chain(client, prompt= formated_prompt)

    conversation_chain = st.session_state["conversation_chain"]
    # Exibe histórico de mensagens
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Captura a entrada do usuário
    if user_message := st.chat_input("Comece a adivinhar"):
        # Adiciona a mensagem do usuário ao histórico
        st.session_state["messages"].append({"role": "user", "content": user_message})

        # Processa a mensagem com o LangChain

        assistant_response = conversation_chain.run(input=user_message)

        # Exibe a mensagem do usuário
        st.chat_message("user").markdown(user_message)

        # Exibe a resposta do assistente
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

        # Adiciona a resposta do assistente ao histórico
        st.session_state["messages"].append({"role": "assistant", "content": assistant_response})


if __name__ == "__main__":
    main()
