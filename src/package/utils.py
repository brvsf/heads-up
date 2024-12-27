import streamlit as st
from src.package.registry import OPTIONS_PT, OPTIONS_EN, difficulty_mapping, template_mapping

class ValueMapper:

    @classmethod
    def difficulty_mapper(cls, difficulty : str) -> list:
        """"""
        return difficulty_mapping.get(difficulty, [])

    @classmethod
    def template_mapper(cls, language : str) -> str:
        """"""
        return template_mapping.get(language, '')

class StreamlitSession:

    @classmethod
    def load_session_state(cls) -> None:
        """"""
        st.session_state.setdefault('language', '')
        st.session_state.setdefault('difficulty', '')
        st.session_state.setdefault('categories', [])
        st.session_state.setdefault('messages', [])

    @classmethod
    def reset_session_state(cls) -> None:
        st.session_state['language'] = ''
        st.session_state['difficulty'] = ''
        st.session_state['categories'] = []
        st.session_state['messages'] = []

class StreamlitUI:

    @classmethod
    @st.dialog("Options")
    def options(cls, language: str) -> None:
        """"""
        if language == 'Portuguese':
            st.session_state['difficulty'] = st.selectbox(label="Dificuldade: ", options=['Facil', 'Médio', 'Dificil'])

            st.session_state['categories'] = st.multiselect(label="Categorias: ", options=OPTIONS_PT, default=OPTIONS_PT[0])

        elif language == 'English':
            st.session_state['difficulty'] = st.selectbox(label="Dificuldade: ", options=['Easy', 'Medium', 'Hard'])

            st.session_state['categories'] = st.multiselect(label="Categorias: ", options=OPTIONS_EN, default=OPTIONS_EN[0])

        if st.button("Concluir"):
            st.rerun()
