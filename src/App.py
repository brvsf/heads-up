import streamlit as st

def main():

    st.set_page_config(page_title= "Heads Up")

    st.session_state['language'] = ''

    st.title("Heads Up")

    if not st.session_state['language']:
        language = st.selectbox("Language Selection:", ['','Português', 'English'])
        st.session_state['language'] = language

if __name__ == '__main__':
    main()
