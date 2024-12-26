import streamlit as st

from src.languages import English, Portuguese
from src.package.utils import StreamlitSession

def page():

    StreamlitSession.load_session_state()

    st.title("Heads Up")

    if not st.session_state['language']:
        st.session_state['language'] = st.selectbox("Language Selection:", ['','Português', 'English'])
        if st.session_state['language']:
            st.rerun()

    if st.session_state['language'] == 'Português':
        Portuguese.main()

    if st.session_state['language'] == 'English':
        English.main()

if __name__ == '__page__':
    page()
