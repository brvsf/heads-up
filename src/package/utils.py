import streamlit as st
from src.package.llm import LLMIntegration
from src.package.registry import OPTIONS_PT, OPTIONS_EN, TEMPLATE_PT,\
    TEMPLATE_EN, HOW_TO_PLAY_PT, HOW_TO_PLAY_EN, template_mapping

class ValueMapper:

    @classmethod
    def template_mapper(cls, language : str) -> str:
        """
        Maps the language to a corresponding template based on the provided language.

        Args:
            language (str): The language to map the template for.

        Returns:
            str: The template string corresponding to the language, or an empty string if not found.
        """
        return template_mapping.get(language, '')

class StreamlitSession:

    @classmethod
    def load_session_state(cls) -> None:
        """
        Initializes session state variables if they do not already exist. This ensures
        that session-related variables such as language, difficulty, prompt, etc., are available.

        Returns:
            None
        """
        st.session_state.setdefault('language', '')
        st.session_state.setdefault('difficulty', '')
        st.session_state.setdefault('prompt', '')
        st.session_state.setdefault('conversation_chain', None)
        st.session_state.setdefault('categories', [])
        st.session_state.setdefault('messages', [])
        st.session_state.setdefault('disable_chat', False)
        st.session_state.setdefault('chat_label', "Comece a adivinhar")

    @classmethod
    def reset_session_state(cls) -> None:
        """
        Resets the session state variables to their default values.

        Returns:
            None
        """
        st.session_state['language'] = ''
        st.session_state['difficulty'] = ''
        st.session_state['prompt'] = ''
        st.session_state["conversation_chain"] = None
        st.session_state['categories'] = []
        st.session_state['messages'] = []
        st.session_state['disable_chat'] = False
        st.session_state['chat_label'] = ''


    @classmethod
    def session_conversation_chain(cls, model, prompt: str):
        """
        Creates and stores a conversation chain in the session state if one does not already exist.

        Args:
            model: The language model to use in the conversation chain.
            prompt (str): The prompt to initialize the conversation.

        Returns:
            None
        """
        if  st.session_state["conversation_chain"] is None:
             st.session_state["conversation_chain"] = LLMIntegration.setup_conversation_chain(model, prompt)

class StreamlitUI:

    @st.dialog("Options")
    def options(language: str) -> None:
        """
        Creates the UI for selecting difficulty, categories, and generating the prompt based on language.

        Args:
            language (str): The language chosen by the user.

        Returns:
            None
        """
        if language == 'Portuguese':
            st.session_state['difficulty'] = st.selectbox(label="Dificuldade: ", options=['Facil', 'Médio', 'Dificil'])

            st.session_state['categories'] = st.multiselect(label="Categorias: ", options=OPTIONS_PT, default=OPTIONS_PT[0])

            st.session_state['prompt'] = TemplateFormat.format_pt(
            st.session_state['categories'],
            st.session_state['difficulty']
            )

        elif language == 'English':
            st.session_state['difficulty'] = st.selectbox(label="Dificuldade: ", options=['Easy', 'Medium', 'Hard'])

            st.session_state['categories'] = st.multiselect(label="Categorias: ", options=OPTIONS_EN, default=OPTIONS_EN[0])

            st.session_state['prompt'] = TemplateFormat.format_en(
            st.session_state['categories'],
            st.session_state['difficulty']
        )

        if st.button("Concluir"):

            st.rerun()

    @st.dialog("How to play")
    def how_to_play(language: str) -> None:
        """
        Displays instructions on how to play the game based on the selected language.

        Args:
            language (str): The language to display the instructions in.

        Returns:
            None
        """
        if language == 'Portuguese':
            st.markdown(HOW_TO_PLAY_PT)
        if language == 'English':
            st.markdown(HOW_TO_PLAY_EN)

class TemplateFormat:

    @classmethod
    def format_pt(cls, categories : list, difficulty : str) -> str:
        """
        Formats the template string for Portuguese using the provided categories and difficulty.

        Args:
            categories (list): A list of categories to include in the prompt.
            difficulty (str): The difficulty level to include in the prompt.

        Returns:
            str: The formatted template string for Portuguese.
        """
        return TEMPLATE_PT.format(categories=", ".join(categories), difficulty=difficulty)

    @classmethod
    def format_en(cls, categories : list, difficulty : str) -> str:
        """
        Formats the template string for English using the provided categories and difficulty.

        Args:
            categories (list): A list of categories to include in the prompt.
            difficulty (str): The difficulty level to include in the prompt.

        Returns:
            str: The formatted template string for English.
        """
        return TEMPLATE_EN.format(categories=", ".join(categories), difficulty=difficulty)
