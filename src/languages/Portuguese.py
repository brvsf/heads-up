import streamlit as st
from src.package.utils import StreamlitUI

def main():

    if not st.session_state['categories'] and not st.session_state['difficulty']:
        StreamlitUI.options(language='Portuguese')

    st.markdown(st.session_state['difficulty'])
    st.markdown(str(st.session_state['categories']))

    if st.button("Options"):
        StreamlitUI.options(language='Portuguese')

if __name__ == "__main__":
    main()
