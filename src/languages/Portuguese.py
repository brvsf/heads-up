import streamlit as st
from src.package.utils import StreamlitUI, StreamlitSession


def main():

    if not st.session_state['categories'] and not st.session_state['difficulty']:
        StreamlitUI.options(language='Portuguese')

    with st.sidebar:
        if st.button("Opções"):
            StreamlitUI.options(language='Portuguese')
        if st.button("Trocar idioma"):
            StreamlitSession.reset_session_state()
            st.rerun()

    # Display chat messages from history on app rerun
    for message in st.session_state['messages']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"GuessMaster: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state['messages'].append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
