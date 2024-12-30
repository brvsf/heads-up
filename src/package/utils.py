import streamlit as st
from src.package.llm import LLMIntegration
from src.package.registry import OPTIONS_PT, OPTIONS_EN, TEMPLATE_PT,\
    TEMPLATE_EN, HOW_TO_PLAY_PT, HOW_TO_PLAY_EN, template_mapping

class ValueMapper:

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
        st.session_state.setdefault('conversation_chain', None)
        st.session_state.setdefault('categories', [])
        st.session_state.setdefault('messages', [])

    @classmethod
    def reset_session_state(cls) -> None:
        st.session_state['language'] = ''
        st.session_state['difficulty'] = ''
        st.session_state["conversation_chain"] = None
        st.session_state['categories'] = []
        st.session_state['messages'] = []

    @classmethod
    def session_conversation_chain(cls, model, prompt: str):
        if st.session_state["conversation_chain"] is None:
             st.session_state["conversation_chain"] = LLMIntegration.setup_conversation_chain(model, prompt)

class StreamlitUI:

    @st.dialog("Options")
    def options(language: str) -> None:
        """"""
        if language == 'Portuguese':
            st.session_state['difficulty'] = st.selectbox(label="Dificuldade: ", options=['Facil', 'Médio', 'Dificil'])

            st.session_state['categories'] = st.multiselect(label="Categorias: ", options=OPTIONS_PT, default=OPTIONS_PT[0])

        elif language == 'English':
            st.session_state['difficulty'] = st.selectbox(label="Dificuldade: ", options=['Easy', 'Medium', 'Hard'])

            st.session_state['categories'] = st.multiselect(label="Categorias: ", options=OPTIONS_EN, default=OPTIONS_EN[0])

        if st.button("Concluir"):
            st.rerun()

    @st.dialog("How to play")
    def how_to_play(language: str) -> None:
        if language == 'Portuguese':
            st.markdown(HOW_TO_PLAY_PT)
        if language == 'English':
            st.markdown(HOW_TO_PLAY_EN)


class TemplateFormat:

    @classmethod
    def format_pt(cls, categories : list, difficulty : str) -> str:
        return TEMPLATE_PT.format(categories=", ".join(categories), difficulty=difficulty)

    @classmethod
    def format_en(cls, categories : list, difficulty : str) -> str:
        return TEMPLATE_EN.format(categories=", ".join(categories), difficulty=difficulty)
