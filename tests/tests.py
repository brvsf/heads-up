import streamlit as st
import src.package.utils as utils
import src.package.registry as registry


class TestValueMapper:

    def test_difficulty_mapper() -> None:
        test_cases = [
            ("Easy", registry.EASY),           # Testing 'Easy'
            ("Fácil", registry.EASY),          # Testing 'Fácil'
            ("Medium", registry.MEDIUM),       # Testing 'Medium'
            ("Médio", registry.MEDIUM),        # Testing 'Médio'
            ("Hard", registry.HARD_INT),       # Testing 'Hard'
            ("Difícil", registry.HARD_BR),     # Testing 'Difícil'
            ("Unknown", []),                   # Testing unkown entry
            ("", []),                          # Testing empty string
            (None, []),                        # Testing None
        ]

        for input_difficulty, expected_output in test_cases:
            result = utils.ValueMapper.difficulty_mapper(input_difficulty)
            assert result == expected_output, f"Failed for {input_difficulty}, expected {expected_output} but got {result}"


        print("test_difficulty_mapper passed successfully ✅")

    def test_template_mapper() -> None:
        test_cases = [
            ("Português", registry.TEMPLATE_PT),    # Testing 'Português'
            ("English", registry.TEMPLATE_EN),      # Testing 'English'
            ("Unknown", ''),                        # Testing unkown entry
            ("", ''),                               # Testing empty string
            (None, ''),                             # Testing None
        ]

        for input_languages, expected_output in test_cases:
            result = utils.ValueMapper.template_mapper(input_languages)
            assert result == expected_output, f"Failed for {input_languages}, expected {expected_output} but got {result}"

        print("test_template_mapper passed successfully ✅")

class TestStreamlitSession:

    def test_load_session_state() -> None:
        st.session_state.clear()
        utils.StreamlitSession.load_session_state()
        expected_state = {
            'language': '',
            'difficulty': '',
            'categories': [],
            'messages': []
        }
        assert st.session_state['language'] == expected_state['language']
        assert st.session_state['difficulty'] == expected_state['difficulty']
        assert st.session_state['categories'] == expected_state['categories']
        assert st.session_state['messages'] == expected_state['messages']

        print("test_load_session_state passed successfully ✅")


    def test_reset_session_state() -> None:
        st.session_state['language'] = 'English'
        st.session_state['difficulty'] = 'Medium'
        st.session_state['categories'] = ['Sports']
        st.session_state['messages'] = ['Hello']
        expected_state = {
            'language': '',
            'difficulty': '',
            'categories': [],
            'messages': []
        }

        utils.StreamlitSession.reset_session_state()

        assert st.session_state['language'] == expected_state['language']
        assert st.session_state['difficulty'] == expected_state['difficulty']
        assert st.session_state['categories'] == expected_state['categories']
        assert st.session_state['messages'] == expected_state['messages']

        print("test_reset_session_state passed successfully ✅")



def main():
    print("Running test functions ⌛")
    #Mapper functions
    TestValueMapper.test_difficulty_mapper()
    TestValueMapper.test_template_mapper()

    # Streamlit Session
    TestStreamlitSession.test_load_session_state()
    TestStreamlitSession.test_reset_session_state()


if __name__ == '__main__':
    main()
