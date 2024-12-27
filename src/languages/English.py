import streamlit as st
from src.package.utils import StreamlitUI, StreamlitSession

def main():

    if not st.session_state['categories'] and not st.session_state['difficulty']:
        StreamlitUI.options(language='English')

    with st.sidebar:
        if st.button("Options"):
            StreamlitUI.options(language='English')
        if st.button("Change language"):
            StreamlitSession.reset_session_state()
            st.rerun()


if __name__ == "__main__":
    main()
