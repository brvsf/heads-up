import src.package.utils as utils
import src.package.registry as registry


class TestValueMapper:

    def test_difficulty_mapper():
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




def main():
    print("Running test functions ⌛")
    TestValueMapper.test_difficulty_mapper()


if __name__ == '__main__':
    main()
