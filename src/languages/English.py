import streamlit as st
from src.package.utils import StreamlitUI

def main():

    if not st.session_state['categories'] and not st.session_state['difficulty']:
        StreamlitUI.options(language='English')

    st.markdown(st.session_state['difficulty'])
    st.markdown(st.session_state['categories'])

    if st.button("Opções"):
        StreamlitUI.options(language='English')

if __name__ == "__main__":
    main()
