import streamlit as st

from src.languages import English, Portuguese

def page():

    st.set_page_config(page_title= "Heads Up")

    st.session_state['language'] = ''

    st.title("Heads Up")

    if not st.session_state['language']:
        language = st.selectbox("Language Selection:", ['','Português', 'English'])
        st.session_state['language'] = language

    if st.session_state['language'] == 'Português':
        Portuguese.main()

if __name__ == '__page__':
    page()
